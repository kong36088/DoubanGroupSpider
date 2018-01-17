# -*- coding: utf-8 -*-

# Scrapy settings for DoubanGroup project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'DoubanGroup'

SPIDER_MODULES = ['DoubanGroup.spiders']
NEWSPIDER_MODULE = 'DoubanGroup.spiders'

ROBOTSTXT_OBEY = True

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.douban.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

# 每个小组抓取的数量
CRAW_NUM = 1000

# 要抓取的group
GROUPS = ['nanshanzufang', 'szsh','106955']

# 速度控制
DOWNLOAD_DELAY = 1

MYSQL_HOST = 'mysql'
MYSQL_DBNAME = 'douban'         #数据库名字，请修改
MYSQL_USER = 'root'             #数据库账号，请修改
MYSQL_PASSWD = 'root'         #数据库密码，请修改
MYSQL_PORT = 3306               #数据库端口，在dbhelper中使用
MYSQL_CHARSET = "utf8mb4"

ITEM_PIPELINES = {
    'DoubanGroup.pipelines.DoubangroupPipeline': 300,#保存到mysql数据库
}

LOG_LEVEL = 'INFO'

LOG_FILE ='log.txt'
