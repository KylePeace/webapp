'''
author:dsf
'''


import pymysql

#1.
# db = pymysql.connect("localhost", user = "root", passwd = 'root', db = "students", port = 3306 )

# cur = db.cursor()


#删除表
#cur.execute("drop table if exists employee") 

# #创建表
# sql = """ create table employee(
#         id int(4)  auto_increment primary key not null,
#         first_name char(20) not null,
#         last_name char(20),
#         age int,    
#         sex char(1),
#         income float)
#     """
# cur.execute(sql)
# db.close()

# #2.
# db = pymysql.connect("localhost", user = "root", passwd = 'root', db = "students", port = 3306 )

# cur = db.cursor()
# sql = " insert into employee(first_name,\
#         last_name,age,sex,income)\
#         values('%s','%s','%d','%c','%d')"%\
#         ("mac",'mohan',20,"m",20000)
# try:
#     cur.execute(sql)
#     db.commit()
# except :
#     #发生错误时回滚

#     db.rollback()
#     print("error....")
# db.close()

# #3.
# #fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
# # fetchall(): 接收全部的返回结果行.
# # rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
# db = pymysql.connect("localhost", user = "root", passwd = 'root', db = "students", port = 3306 )
# cur = db.cursor()
# sql = "select *from employee where income > '%d'"%(1000)

# try:
#     cur.execute(sql)
#     results = cur.fetchall()
#     # results = cur.fetchone()
#     #print(cur.rowcount)
#     for row in results:
#         print(row)
# except:
#     print("error .....")
# db.close()

#4
# db = pymysql.connect("localhost", user = "root", passwd = 'root', db = "students", port = 3306 )
# cur = db.cursor()

# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 where sex  = \
#     '%c'"%('M')
# try:
#     cur.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# db.close()

#5
# db = pymysql.connect("localhost", user = "root", passwd = 'root', db = "students", port = 3306 )
# cur = db.cursor()

# sql = "delete from  employee where age < %d "%(5)

# try:
#     cur.execute(sql)
#     db.commit()
# except Exception as e:
#     print(e)
#     print("error////")
#     db.rollback()

# db.close()

print("test.py execute over")

