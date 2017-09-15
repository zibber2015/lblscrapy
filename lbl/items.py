# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LblItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #url = scrapy.Field()
    title = scrapy.Field()
    #name = scrapy.Field()
    #head = scrapy.Field()
    content = scrapy.Field()
    page = scrapy.Field()
    img = scrapy.Field()
    text = scrapy.Field()


