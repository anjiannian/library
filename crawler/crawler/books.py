# -*- coding: utf-8 -*-

import scrapy

class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["douban.com", "book.douban.com"]
    start_urls = [
        "urls"
    ]

    def parse(self, response):
        pass
