# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SousuoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    key_words = scrapy.Field()
    content = scrapy.Field()
    Catalog = scrapy.Field()
    page = scrapy.Field()
    wiki_content = scrapy.Field()
    wiki_Catalog = scrapy.Field()
    wiki_key_words = scrapy.Field()




