#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Загрузка необходимых библиотек
import codecs
codecs.register(
    lambda name: name == 'cp65001' and codecs.lookup('UTF-8') or None
)
# Проверка работы
print("Я робот")
# Загрузка необходимых библиотек
import lxml
from lxml import html
from lxml import etree
from lxml.html import fromstring
from lxml.html import tostring
from urllib.request import urlopen
import urllib3	
import requests
import certifi
import xlsxwriter
import multiprocessing
from urllib.parse import urljoin
from user_agents import parse
import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import threading
import itertools
import sys
try:
        # python 3
	sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
except:
        # python 2
	sys.stdout = codecs.getwriter('utf8')(sys.stdout)
start = time.time()
# Время старта
print(start)
# Эмуляция браузера
headers = urllib3.make_headers(user_agent='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6')
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
# 
ua_string = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6)  Gecko/20070725 Firefox/2.0.0.6'
user_agent = parse(ua_string)
base_url = "https://www.reformagkh.ru/myhouse?tid=2354521&sort=name&order=asc&page=%s"

class Proxy(object):
	proxy_url = 'https://www.ip-adress.com/proxy-list'
	proxy_list = []

	def __init__(self):
		page = requests.get(self.proxy_url)
		tree = lxml.html.document_fromstring(page.content)
		prox = tree.xpath('//html/body/main/table/tbody/tr/td[1]')
		prox2 = [proxy.text_content().replace("\n","</a>") for proxy in prox]
		self.proxy_list = prox2

	def get_proxy(self):
		for prox3 in self.proxy_list:
			url = 'http://' + prox3
			print('this proxy' + url)
			try:
				r = requests.get('http://speed-tester.info/check_ip.php', proxies={'http':url})
				if r.status_code==200:
			  		return url
			except requests.exceptions.ConnectionError:
				continue
prox3 = Proxy()
prox3 = prox3.get_proxy()
print(prox3)
base_url = "https://www.reformagkh.ru/myhouse?tid=2354521"
r1 = requests.get(base_url, proxies={'http':prox3})
print(r1.text)

