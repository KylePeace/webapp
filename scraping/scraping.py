#四
# 3.1
# import requests
# r = requests.get('http://www.santostang.com/')
# print("文本编码：",r.encoding)
# print("状态响应码：",r.status_code)
# #print("字符串方式的响应体：",r.text)
# print(r.content)


# 3.2
# import requests
# key_dict = {'key1': "value1", "key2": "value2"}
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
# r = requests.get("http://httpbin.org/get", params=key_dict)
# print("URL已经正确编码：", r.url)
# print("字符串方式响应体：", r.text)


# 3.2.2请求头
# import requests
# key_dict = {'key1': "value1", "key2": "value2"}
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
#     'Host' : 'www.santostang.com'
#     }
# r = requests.get("http://www.santostang.com/", headers =headers)
# print("URL已经正确编码：", r.url)
# print("字符串方式响应体：", r.text)

# 3.3.3 发送post请求
# '''
# 目的：例如：再登陆时候请求，如果用密码的话会暴露再url中非常不安去，所以用
# post 请求，post请求需要传递参数
# '''
# import requests
# key_dict = {'key1' : "value1",'key2' : 'value2' }
# r = requests.post("http://httpbin.org/post",data=key_dict)
# print(r.text)

# #3.3.4 超时问题
# '''
#     若遇到服务器长时间不返回，这时候爬虫程序就会一直等待，造成爬虫程序没有顺利执行，因此，可用Requests
#     在timeout参数设定的秒数结束之后停止等待的响应。也就是如果服务器在timeout秒内没有应答，就返回异常。
#  '''
# import requests
# link = "http://www.santostang.com/"
# r = requests.get(link,timeout = 0.5)
# print(r.text)

# 3.4 Requests 爬虫实践：top250电影数据
# 3.4.2项目实践爬取豆瓣数据
# import requests
# from bs4 import BeautifulSoup

# def getMovie():
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
#         "Host": "movie.douban.com"
#     }
#     movie_list = []
#     dector_list = []
#     for i in range(0,10):

#         link = "http://movie.douban.com/top250?start=" + \
#             str(i * 25) + "&filter=";
#         r = requests.get(link,headers = headers,timeout = 10)
#         print(str(i+1),"状态响应码:",r.status_code)
#         soup = BeautifulSoup(r.text, "lxml")
#         div_item = soup.find_all('div', attrs={'class': 'item'})

#         for each in div_item:
#             div_list = each.find_all('div', attrs={'class': 'hd'})
#             print(div_list[0].a.span.text.strip())
#             div_director = each.find_all('div', attrs={'class': 'bd'})
#             print(div_director[0].p.text.strip())

# getMovie()

#四
#4.3.1
# selenium  使用 需要下载geckodriver
# from selenium import webdriver

# chromepath = r"C:\Users\hukai\AppData\Local\Google\Chrome\Application\chrome.exe"


# driver = webdriver.Chrome()

# driver.get("http://www.santostang.com/2017/03/02/hello-world/")

# print(driver.title)

# driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
# comment = driver.find_element_by_css_selector('div.reply-content')
# content = comment.find_element_by_tag_name('p')
# print(content.text)
#driver.quit()


#4.3.3
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("http://www.santostang.com/2017/03/02/hello-world/")
# driver.switch_to.frame(
#     driver.find_element_by_css_selector("iframe[title='livere']"))
# comments = driver.find_elements_by_css_selector('div.reply-content')

# for each in comments:
#     content = each.find_element_by_tag_name('p')
#     print (content.text)
# driver.quit()

#4.3.4
# from selenium import webdriver
# # caps = webdriver.DesiredCapabilities().CHROME
# # caps["marionette"] = False

# co = webdriver.ChromeOptions()

# driver = webdriver.Chrome()
# driver.get("http://www.santostang.com/2017/03/02/hello-world/")
# driver.quit()

# print("game over")

# #4.3.5 练习
# #爬取深圳爱比邻数据，房源名称，价格，评价数量，房屋类型，床数量，房客数量,爬取20页数据，动态网页爬取
# #动态网页与静态网页的区别 ：动态网页加载有时候使用的是json，不是在html中
# from selenium import webdriver
# import time

# nowtime = time.time()
# #不显示图片
# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images": 2}
# chrome_options.add_experimental_option("prefs", prefs)

# #driver = webdriver.Chrome(executable_path = chromepath,chrome_options = chrome_options
# driver = webdriver.Chrome(chrome_options=chrome_options)

# URL = "https://zh.airbnb.com/s/%E4%B8%AD%E5%9B%BD%E5%B9%BF%E4%B8%9C%E7%9C%81%E6%B7%B1%E5%9C%B3%E5%B8%82/homes?place_id=ChIJkVLh0Aj0AzQRyYCStw1V7v0&allow_override%5B%5D=&s_tag=p1wmjt4M&cdn_cn="

# ret_list = []
# for x in range(0,20):
#     driver.get(URL+"1")
#     ret_list = driver.find_elements_by_css_selector("div._1mpo9ida")
#     for eachhouse in ret_list:
#         try:
#             comment = eachhouse.find_element_by_css_selector("span._gb7fydm")
#             comment = comment.text
#         except:
#             comment = "new"

#         price = eachhouse.find_element_by_css_selector("span._hylizj6")
#         price = price.text
#         name = eachhouse.find_element_by_css_selector("span._a4k7y39")
#         name = name.text
#         details = eachhouse.find_element_by_css_selector("span._1127fdt6")
#         details = details.text

#         print(name)
#         print("评论数：" + comment)
#         print(price)
#         print(details)   
#         print("   ")
#         print("   ")
# driver.quit()
# print("爬取爱比邻数据结束！")
# usetime = time.time() - nowtime
# print("共用时:%秒" %usetime)

#五.解析网页
#5.1 使用正则表达式解析网页
# '''
# . : 匹配任意字符，除了换行符
# * ：匹配前一个字符0次或者多次
# + ：匹配前一个字符1次或者多次
# ？ ：匹配前一个字符0次或者1次
# ^ ：匹配字符串开头
# $ ：匹配字符串末尾
# ():匹配括号内的表达式，也表示一个组
# \s :匹配空白字符
# \S :匹配任何非空白字符
# \d :匹配数字，等价于｛0-9｝
# \D :匹配任何非数字，等价于｛^0-9｝
# \w :匹配字母数字，等价于[A-Za-z0-9]
# \W :匹配非字母数字，等价于[^A-Za-z0-9]
# [] :用来表示一组字符
# '''
#正则练习
#re.match(pattern, string, flags=0) flags:用来控制正则表达式的匹配方式，如：是否区分大小写，多行匹配
#re.search()

# 练习1
# import re
# m = re.match('www',"www.santostang.com")
# print("匹配结果：", m)
# print("匹配的起始和终点：", m.span())
# print("匹配的起始位置：", m.start())
# print("匹配的终点位置：", m.end())

# #练习2
# import re
# line = "Fat cats are smarter than dogs, is it right?"
# m = re.match(r'(.*) are (.*?) dogs', line)
# #m = re.match(r'(.?) are', line)

# print("匹配的整句话：", m.group())
# print("匹配的第一句话：", m.group(1))
# print("匹配的第二句话：", m.group(2))
# print("匹配的结果列表：", m.groups())

# #练习3
# # match:只能从字符串的起始位置进行匹配
# # search：扫描整个字符串并返回第一个成功匹配
# import re
# m_match = re.match("com",'www.santostang.com')
# m_search = re.search("com", 'www.santostang.com')
# print(m_match)
# print(m_search)

#练习4
# #match,search 匹配一个返回
# #findall 匹配所有可能的对象返回
# import re
# m_match = re.match('[0-9]+','12345 is the first number,23456 is the sencond')
# m_search = re.search('[0-9]+','12345 is the first number,23456 is the sencond')
# m_findall = re.findall('[0-9]+','12345 is the first number,23456 is the sencond')

# print(m_match.group())    # 123456
# print(m_search.group())   # 123456
# print(m_findall)  # ['12345', '23456']

#5.2使用BeautifulSoup解析网页
# #练习1
# import requests
# from bs4 import BeautifulSoup

# link = "http://www.santostang.com/"
# headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"}
# r = requests.get(link,headers = headers)

# soup = BeautifulSoup(r.text,"html.parser")
# # print(soup)
# # print(soup.prettify())
# first_title = soup.find("h1",class_ = "post-title").a.text.strip()
# print("第一篇文章的标题是：",first_title)

# title_list = soup.find_all("h1", class_="post-title")
# for title in title_list:
#     print(title.a.text.strip())


# #5.3 lxml的使用
# #练习1
# import requests
# from lxml import etree
# link = "http://www.santostang.com/"
# headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"}
# r = requests.get(link,headers = headers)
# html = etree.HTML(r.text)
# title_list = html.xpath('//h1[@class ="post-title"]/a/text()')
# print(title_list)


# #5.5 使用Beautifusoup 爬取数据
# #爬取安客居网站深圳二手房数据：房源名称，价格，几房几厅，大小，建造年份，联系人，地址，标签。
# import requests
# from bs4 import BeautifulSoup
# link = "https://shenzhen.anjuke.com/sale/p%d/"
# headers = {
#     'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"}

# for index in range(1,10):  
#     print("index====%d"%index) 
#     r = requests.get(link % index, headers=headers)
#     soup = BeautifulSoup(r.text,"lxml")
#     house_list = soup.find_all("li", class_ ="list-item")
#     for house in house_list:
#         print(" ")
#         name = house.find("div", class_="house-title").a.text.strip()
#         url = house.find("div", class_="house-title").a.attrs["href"]
#         price = house.find("span", class_="price-det").text.strip()
#         price_area = house.find("span", class_="unit-price").text.strip()
#         no_room = house.find("div", class_="details-item").span.text.strip()
#         area = house.find("div", class_="details-item").contents[3].text.strip()
#         floor = house.find("div", class_="details-item").contents[5].text.strip()
#         try:
#             year = house.find("div", class_="details-item").contents[7].text.strip()
#         except :
#             year = "没有年份"
#         broker = house.find("span", class_="brokername").text.strip()
#         address = house.find("span", class_="comm-address").text.strip()
#         address = address.replace("\xa0\xa0\n            "," ")
#         tag_list = house.find_all("span", class_="item-tags tag-others")
#         tags = [i.text for i in tag_list]
#         r2 = requests.get(url, headers=headers)
#         soup2 = BeautifulSoup(r2.text, "lxml")
#         special = soup2.find("div", class_ =  "houseInfoV2-item-desc js-house-explain").text
#         special = "核心特色："+special
#         print(name, url,price, price_area, no_room, area, floor, year, broker, address\
#             , tags)
#         print(special)

#六.数据存储
#txt
# title = "this is a test sentence"
# with open('C:\\Users\\hukai\\Desktop\\title.txt',"a+") as f:
#     f.write(title)
#     f.close()

# output = "\t".join(["name","age","sex"])
# with open(r'C:\Users\hukai\Desktop\title.txt',"a+") as f:
#     f.write("s"+r"\n")
#     f.write(output)
#     f.close()

# with open(r'C:\Users\hukai\Desktop\title.txt', "r") as f:
#     result =f.read()
#     print(result)

#csv
# import csv
# with open(r'C:\Users\hukai\Desktop\test.csv',"r",encoding="UTF-8") as csvfile:
#     csv_reader = csv.reader(csvfile)
#     for row in csv_reader:
#         print(row)
#         print(row[0])


#mongo数据库操作
import requests
import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient("localhost",27017)
db = client.blog_database
collection = db.blog

link = "http://www.santostang.com/"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"}
r = requests.get(link,headers = headers)

soup = BeautifulSoup(r.text,"lxml")
title_list = soup.find_all("h1",class_ = "post-title")
for eachone in title_list:
    url = eachone.a["href"]
    title = eachone.a.text.strip()
    post = {"url":url,"title":title,"date":datetime.datetime.utcnow()}
    collection.insert_one(post)