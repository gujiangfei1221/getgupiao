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
            list = [tmp[0],tmp[1],tmp[2],tmp[3],tmp[4]]
        f.close()
        f2 = open('result2/'+filename,'r+')
        list.append(f2.readline())
        f2.close()

        list2 = []
        for i in list:
            list2.append(i.strip())

        # print('insert into gupiaoinfo(gupiaoname,latestlowprice,latesthighprice,longlowprice,price) values(\''+list2[0]+'\',\''+list2[3]+'\',\''+list2[2]+'\',\''+list2[5]+'\',\''+list2[4]+'\')')

        try:
        #获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
            conn=pymysql.connect(host='localhost',user='root',passwd='root',db='codeigniter',port=3306,charset='utf8')
            cur=conn.cursor()#获取一个游标
            # cur.execute("update gupiaoinfo set latestlowprice = list[3],latesthighprice = list[2],price = list[4],longlouwprice = list[5] where gupiaoname = list[0]")
            cur.execute("insert into gupiaoinfo(gupiaoname,latestlowprice,latesthighprice,longlowprice,price) values(\'"+list2[0]+'\',\''+list2[3]+'\',\''+list2[2]+'\',\''+list2[5]+'\',\''+list2[4]+'\')')
            conn.commit();
            cur.close()#关闭游标
            conn.close()#释放数据库资源
        except  Exception:
            raise
print('ok!!!!!!!!!!!!!!!!!')