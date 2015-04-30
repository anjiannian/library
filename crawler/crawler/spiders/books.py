# -*- coding: utf-8 -*-

import os
import json

import scrapy
from scrapy.http import Request
from scrapy.selector import Selector

from crawler.items import Book


PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
URL = "https://api.douban.com/v2/book/isbn/"


def get_start_urls():
    res = []
    with open(os.path.join(PATH, "finally.txt")) as urlsfile:
        for line in urlsfile:
            res.append(line)
    return res


class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["douban.com", "book.douban.com"]
    start_urls = get_start_urls()

    def parse(self, response):
        sel = Selector(response)

        # Go to certain url for book details to get isbn
        book_urls = sel.xpath("//div[@class='mod book-list']/dl/dt/a/@href")
        for url in book_urls:
            yield Request(url, callback=self.parse_isbn)

        # Get next page and do it again
        more_page = sel.xpath("//span[@class='next']/a/@href")
        if more_page:
            yield Request(more_page, callback=self.parse)

    def parse_isbn(self, response):
        sel = Selector(response)

        xpath = "//div[@id='info']/span[position()=last()]/\
            following-sibling::text()"
        isbn = sel.xpath(xpath)[0].strip()
        yield Request(URL + isbn, callback=self.parse_book)

    def parse_book(self, response):
        data = json.loads(response.body)
        book = Book()
        book['title'] = data['title']
        book['subtitle'] = data['subtitle']
        book['origin_title'] = data['origin_title']
        book['author'] = data['author']
        book['translator'] = data['translator']
        book['publisher'] = data['publisher']
        book['pubdate'] = data['pubdate']
        book['pages'] = data['pages']
        book['price'] = data['price']
        book['summary'] = data['summary']
        book['series'] = data['series']
        book['binding'] = data['binding']
        book['isbn10'] = data['isbn10']
        book['isbn13'] = data['isbn13']
        yield book
