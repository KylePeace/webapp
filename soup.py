#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys



headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
res = requests.get('https://nba.hupu.com/',headers)
print(res.encoding)
res.encoding = 'utf-8'
print(res.text)

soup = BeautifulSoup(res.content,"html.parser")
print(soup.text)
