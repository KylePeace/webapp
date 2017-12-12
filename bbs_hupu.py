from bs4 import BeautifulSoup
from  pymongo import MongoClient
import requests

def soup_1(link):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)\
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    r = requests.get(link,headers = headers)
    r.encoding = "UTF-8"
    soup = BeautifulSoup(r.text,"lxml")
    return  soup

def get_page_data(data_list,post_list):
    link_front = "https://bbs.hupu.com"
 
    for post in post_list:
        data = {}
        title = post.find("a",class_ = "truetit").text.strip()
        title_link = link_front + post.find("a",class_ = "truetit")["href"].strip()
        author = post.find("a",class_ = "aulink").text.strip()
        author_link =   post.find("a",class_ = "aulink")["href"].strip()
        date = post.find_all("div","author box")[0].find_all("a")[1].text.strip()
        reply_view = post.find("span",class_="ansour box").text.strip()
        reply = reply_view.split("/")[0]
        view = reply_view.split("/")[1]
        last_reply = post.find("span",class_ = "endauthor").text.strip() 

        data["title"] = title
        data["title_link"] = title_link
        data["author"] = author
        data["author_link"] = author_link
        data["date"] = date
        data["reply"] = reply
        data["view"] = view
        data["last_reply"] = last_reply
        
                
        # data.insert(0, title)
        # data.insert(1,title_link) 
        # data.insert(2,author) 
        # data.insert(3,author_link) 
        # data.insert(4,date) 
        # data.insert(5,reply) 
        # data.insert(6,view) 
        # data.insert(7,last_reply) 

        data_list.append(data)
    return  data_list
    
def connect_mogodb():
    conn = MongoClient("localhost",27017)
    db = conn.mydb
    my_set = db.hupu_bbs
    return my_set


#prettify()

if __name__ == '__main__':
    link_home = "https://bbs.hupu.com/digital-"
    data_list = []
    for index in range(1,11):
        link = link_home + str(index)
        html = soup_1(link)
        post_list = html.find("ul",class_="for-list").find_all("li")
        data_list = get_page_data(data_list,post_list)
        #print(data_list)
        print(index)
    #print(data_list)
    my_set = connect_mogodb()
    my_set.insert(data_list)

