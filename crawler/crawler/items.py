# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Book(scrapy.Item):
    title = scrapy.Field()
    publisher = scrapy.Field()
    isbn10 = scrapy.Field()
    isbn13 = scrapy.Field()
    price = scrapy.Field()
    binding = scrapy.Field()
    translator = scrapy.Field()
    pubdate = scrapy.Field()
    author = scrapy.Field()
    subtitle = scrapy.Field()
    origin_title = scrapy.Field()
    pages = scrapy.Field()
    summary = scrapy.Field()
    series = scrapy.Field()


class Series(scrapy.Item):
    title = scrapy.Field()
