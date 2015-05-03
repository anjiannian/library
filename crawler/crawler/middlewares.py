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
        log.msg("++++++++++++++++++++++", level=log.DEBUG)
        self.proxies = get_proxy()

    def process_request(self, request, spider):
        if 'proxy' in request.meta:
            return
        request.meta['proxy'] = random.choice(self.proxies)

    def process_exception(self, request, exception, spider):
        proxy = request.meta['proxy']
        log.msg('Removing failed proxy <%s>, %d proxies left' % (
            proxy, len(self.proxies)))
        try:
            self.proxies.remove(proxy)
        except ValueError:
            pass


def is_bad_proxy(proxy):
    try:
        proxy_handler = urllib2.ProxyHandler({'http': proxy})
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)
        req = urllib2.Request('http://www.baidu.com')
        urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print 'Error code: ', e.code
        return e.code
    except Exception, detail:
        print "ERROR:", detail
        return True
    return False


def get_proxy():
    socket.setdefaulttimeout(5)
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
        proxies.extend(list(input))
    proxies = list(set(proxies))
    for proxy in proxies:
        if is_bad_proxy(proxy):
            proxies.remove(proxy)
    with open(proxy_file, 'w') as output:
        for proxy in proxies:
            output.write(proxy + '\n')
    return proxies

if __name__ == '__main__':
    get_proxy()
