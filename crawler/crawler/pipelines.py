# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime

import MySQLdb
from scrapy import log


class CrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class MySQLPipeline(object):

    def __init(self):
        self.conn = MySQLdb.connect(
            user='nobody', db='dbname', host='127.0.0.1',
            charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        create_time = datetime.now()
        try:
            self.cursor.execute(
                """
                INSERT INTO book (title, subtitle, title, subtitle,
                    origin_title, author, translator, publisher, pubdate,
                    pages, price, summary, series, binding, isbn10, isbn13,
                    created) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (item['title'].encode('utf-8'),
                      item['subtitle'].encode('utf-8'),
                      item['origin_title'].encode('utf-8'),
                      item['author'].encode('utf-8'),
                      item['translator'].encode('utf-8'),
                      item['publisher'].encode('utf-8'),
                      item['pubdate'],
                      item['pages'],
                      item['price'],
                      item['summary'].encode('utf-8'),
                      item['series'].encode('utf-8'),
                      item['binding'].encode('utf-8'),
                      item['isbn10'],
                      item['isbn13'], create_time))
            self.conn.commit()
            log.msg("Sucess: %s, %s" % (item['isbn13'], item['title']),
                    level=log.INFO)
        except MySQLdb.Error, e:
            log.msg("Error: %d: %s" % (e.args[0], e.args[1]), level=log.ERROR)

        return item
