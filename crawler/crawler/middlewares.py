# -*- coding: utf-8 -*-

import os
import random

PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
proxy_file = os.path.join(PATH, 'proxies.txt')

class ProxyMiddleware(object):

    def process_request(self, request, spider):
        proxy = ProxyList.produce()
        request.meta['proxy'] = proxy

class ProxyList(object):

    def __init__(self):
        self.proxies = self.test()

    def produce():
        proxy = random.choice(self.proxies)


    def test():
        with open(proxy_file, 'wr') as proxies:
            for line in proxies:



