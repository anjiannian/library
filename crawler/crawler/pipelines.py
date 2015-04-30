# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from datetime import datetime

import MySQLdb
from scrapy import log
from scrapy.conf import settings


class CrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class MySQLPipeline(object):

    def __init__(self):
        self.conn = MySQLdb.connect(
            user=settings['MYSQL_USER'], db=settings['MYSQL_DB'],
            host=settings['MYSQL_SERVER'], passwd=settings['MYSQL_PASSWD'],
            charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        log.msg("-------------------------", level=log.DEBUG)
        create_time = datetime.now()
        try:
            self.cursor.execute(
                """
                INSERT INTO book (title, subtitle, origin_title, author,
                    translator, publisher, pubdate, binding, price,
                    pages, summary, series, isbn10, isbn13, created) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (item['title'].encode('utf-8'),
                      item['subtitle'].encode('utf-8'),
                      item['origin_title'].encode('utf-8'),
                      json.dumps(item['author']),
                      json.dumps(item['translator']),
                      item['publisher'].encode('utf-8'),
                      item['pubdate'],
                      item['binding'].encode('utf-8'),
                      item['price'],
                      item['pages'],
                      item['summary'].encode('utf-8'),
                      json.dumps(item['series']),
                      item['isbn10'],
                      item['isbn13'], create_time))
            self.conn.commit()
            log.msg("Sucess: %s, %s" % (item['isbn13'], item['title']),
                    level=log.INFO)
            log.msg("*************************", level=log.DEBUG)
        except MySQLdb.Error, e:
            log.msg("Error: %d: %s" % (e.args[0], e.args[1]), level=log.ERROR)

        return item
