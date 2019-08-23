#mysql数据库示例
# -*- coding: utf-8 -*-
import mysql.connector
import logging

usr=input('请输入用户名:')
pwd=input('请输入密码:')

conn=mysql.connector.connect(host='144.34.158.32',user=usr,password=pwd,database='test')
cursor=conn.cursor()
#创建user表
try:
    cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
except Exception as e:
    print('表已存在')

#插入数据
try:
    cursor.execute('insert into user(id,name)values(%s,%s)',['1','Michael'])
except Exception as e:
    print('id已存在')

if cursor.rowcount > 0:
    print('*********')
    print('%s行被插入'% (cursor.rowcoun))
    print('*********')
else:
    print('没有数据改变')
#提交事务
conn.commit()
cursor.close()
#执行查询
cursor=conn.cursor()
cursor.execute('select * from user where id = %s',('1',))
values=cursor.fetchall()

print(values)
#关闭cursor和数据库连接
cursor.close()
conn.close()
