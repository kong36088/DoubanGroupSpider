# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

import pymysql
from . import settings


def filter_emoji(src):
    try:
        # UCS-4
        highpoints = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
    except re.error:
        # UCS-2
        highpoints = re.compile(
            u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')
    # mytext = u'<some string containing 4-byte chars>'
    return highpoints.sub(u'\u25FD', src)


class DoubangroupPipeline(object):
    def get_db_conn(self):
        conn = pymysql.connect(
            host=settings.MYSQL_HOST,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset=settings.MYSQL_CHARSET,
            use_unicode=False,
            database=settings.MYSQL_DBNAME
        )
        return conn

    def process_item(self, item, spider):
        db_con = self.get_db_conn()
        cursor = db_con.cursor()
        sql = "REPLACE INTO `group`(url,group_id,title,author,reply_num,last_reply_time) VALUES(%s,%s,%s,%s,%s,%s)"
        try:
            title = filter_emoji(item['title'])
            author = filter_emoji(item['author'])

            cursor.execute(sql, (item['url'], item['group_id'], title,
                                 author, item['reply_num'], item['last_reply_time']))
            cursor.connection.commit()
        except BaseException as e:
            print("错误在这里>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<错误在这里")
            db_con.rollback()
        return item
