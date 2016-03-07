#-*- coding=utf-8 -*-
import pymysql
import os.path

rootdir = 'result/'

for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        list = []
        f = open('result/'+filename,'r+')
        for i in f.readlines():
            tmp = i.split('#')
            list.append(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4])
        f.close()
        f2 = open('result2/'+filename,'r+')
        list.append(f2.readline())
        f2.close()
        try:
        #获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
            conn=pymysql.connect(host='localhost',user='root',passwd='root',db='codeigniter',port=8889,charset='utf8')
            cur=conn.cursor()#获取一个游标
            cur.execute("update gupiaoinfo set latestlowprice = list[3],latesthighprice = list[2],price = list[4],latesthighprice = list[5] where gupiaoname = list[0]")
            cur.close()#关闭游标
            conn.close()#释放数据库资源
        except  Exception :print("发生异常")
