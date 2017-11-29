# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubangroupItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    group_id = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    reply_num = scrapy.Field()
    last_reply_time = scrapy.Field()
