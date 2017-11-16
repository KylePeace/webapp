
#! /usr/bin/env python
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

res = requests.get('https://nba.hupu.com/',headers)
#print(res.encoding)
res.encoding = 'utf-8'
#print(res.text)

soup = BeautifulSoup(res.content,"html.parser")

#print(soup.text)\
news = soup.select(".nba-news-list")
# print(news[0].text)
# print(news[0].href)
# print(len(news[0]))
for item in news[0]:
    print(item)
    print(item.next)
    
