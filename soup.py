
#! /usr/bin/env python
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
from CreateExcelData import *

data = []

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
for item in news[0].select("a"): #选择a标签
   
    #print(item)
    #print(item.text)
    #获取网页链接
    #print(item["href"])
    #print("-------------------------------------")
    nPos = item["href"].find("https://bbs.hupu.com/")
    #print(nPos)
    if nPos != 0:
        continue
    print("-------------------------------------")
    print("标题："+item.text)
    print("链接："+item["href"])
    real = requests.get(item["href"],headers)
    soup2 = BeautifulSoup(real.content,"html.parser")
    #print(soup2)
    #print(soup2.select(".floor_box"))
    #print(len(soup2.select(".floor_box")))
    name = soup2.select(".floor_box")[0].select(".u")[0].text
    print("楼主："+name)

    #print("评论数："+soup2.select(".bbs-hd-h1")[0])
    print("评论数："+soup2.select(".bbs-hd-h1")[0].select("span")[1].text.strip("回复"))

    #print(soup2.select(".case")[0])
    print("正文：")
    
    #print(soup2.select(".quote-content")[0].select("p")[0].text,end = '')
    if len(soup2.select(".quote-content"))<=0 or  len(soup2.select(".quote-content")[0].select("p"))<=0:
        continue

    for content in soup2.select(".quote-content")[0].select("p")[0].text:
        if content == "，":
            print("\n")
        else:
            print(content,end='')

    print("\n"*2)

    itemData=[item.text,item["href"],name,soup2.select(".bbs-hd-h1")[0].select("span")[1].text.strip("回复"),soup2.select(".quote-content")[0].select("p")[0].text]
    #print(itemData)
    data.append(itemData)

print(data)
excel = CreateExcelData("news", "excel/news.xls")
title = ["标题","链接","楼主","评论数","正文"]

cur_row = 0
for item in title: #表头
    excel.write_to_excel(0, cur_row, item)
    cur_row += 1

cur_row = 0
cur_col = 3
for itemlist in data:#内容
    for item in itemlist:
        excel.write_to_excel(cur_col, cur_row, item)
        cur_row += 1
    cur_row = 0
    cur_col += 1
excel.save_excel()
