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
# selenium  使用              