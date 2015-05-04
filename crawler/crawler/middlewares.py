# -*- coding: utf-8 -*-

import os
import random
import socket
import urllib2
import requests

from scrapy import log
from lxml import html

PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
proxy_file = os.path.join(PATH, 'proxies.txt')


class ProxyMiddleware(object):

    def __init__(self):
        self.proxies = get_proxy()

    def process_request(self, request, spider):
        if 'proxy' in request.meta:
            return
        while not 'proxy':
            self.proxies = get_proxy()
        request.meta['proxy'] = 'http://' + random.choice(self.proxies)
        log.msg("----|%s|||%s|----" % (request.meta['proxy'], request.url),
                level=log.DEBUG)

    def process_exception(self, request, exception, spider):
        proxy = request.meta['proxy']
        log.msg('Removing failed proxy <%s>, %d proxies left' % (
            proxy, len(self.proxies)), level=log.INFO)
        try:
            self.proxies.remove(proxy[7:])
        except ValueError:
            pass


def is_bad_proxy(proxy):
    try:
        proxy_handler = urllib2.ProxyHandler({'http': proxy})
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)
        req = urllib2.Request('http://www.douban.com')
        urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print 'Error code: ', e.code
        return True
    except Exception, detail:
        print "ERROR:", detail
        return True
    return False


def get_proxy():
    socket.setdefaulttimeout(3)
    resp = requests.get("http://cn-proxy.com/")
    root = html.fromstring(resp.content)
    xpath = "//table[@class='sortable']/tbody/tr/td[position()=1 or position()=2]"
    res = root.xpath(xpath)
    res = [ele.text_content() for ele in res]
    proxies = []
    for i in range(0, len(res), 2):
        proxy = res[i] + ':' + res[i+1]
        proxies.append(proxy)
    with open(proxy_file, 'r') as input:
        for line in input:
            proxy = line.strip()
            if proxy not in proxies:
                proxies.append(proxy)
    result = []
    for proxy in proxies:
        if not is_bad_proxy(proxy):
            result.append(proxy)
    with open(proxy_file, 'w') as output:
        for proxy in result:
            output.write(proxy + '\n')
    return result

if __name__ == '__main__':
    get_proxy()
