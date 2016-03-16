#-*- coding=utf-8 -*-
import pymysql
import os.path
import time

rootdir = 'result/'

for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        list = []
        f = open('result/'+filename,'r+')
        for i in f.readlines():
            tmp = i.split('#')
            list = [tmp[0].strip(),tmp[1].strip(),tmp[2].strip(),tmp[3].strip(),tmp[4].strip()]
        f.close()
        f2 = open('result2/'+filename,'r+')
        list.append(f2.readline().strip())
        f2.close()
        if((float(list[2])-float(list[3])) != 0):
            jiazhipaixu1 = (float(list[2])-float(list[4]))/(float(list[2])-float(list[3]))
        else:
            jiazhipaixu1 = 0

        if(float(list[5]) != 0):
            fengxianpaixu1 = (float(list[5])- float(list[4]))/float(list[5])
        else:
            fengxianpaixu1 = 0

        f3 = open('result3/'+filename, 'a+')
        f3.write(str(jiazhipaixu1)+'#'+str(fengxianpaixu1)+'#'+time.strftime("%Y-%m-%d", time.localtime())+'#')
        f3.write('\n')
        f3.close()

        #['gupiaoname','gupiaono','latesthighprice','latestlowprice','price','longhighprice','jiazhipaixu','fengxianpaixu']
        # print('insert into gupiaoinfo(gupiaoname,latestlowprice,latesthighprice,longlowprice,price) values(\''+list2[0]+'\',\''+list2[3]+'\',\''+list2[2]+'\',\''+list2[5]+'\',\''+list2[4]+'\')')
        # print('update gupiaoinfo set latestlowprice ='+ list[3]+',latesthighprice ='+ list[2]+',price = '+ list[4]+',longlowprice ='+ list[5]+',jiazhipaixu ='+ str(jiazhipaixu1)+' ,fengxianpaixu = '+ str(fengxianpaixu1)+' where gupiaoname =\''+ list[0]+'\'')

        try:
        #获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
            conn=pymysql.connect(host='localhost',user='root',passwd='root',db='codeigniter',port=3306,charset='utf8')
            cur=conn.cursor()#获取一个游标
            cur.execute('update gupiaoinfo set latestlowprice ='+ list[3]+',latesthighprice ='+ list[2]+',price = '+ list[4]+',longlowprice ='+ list[5]+',jiazhipaixu ='+ str(jiazhipaixu1)+' ,fengxianpaixu = '+ str(fengxianpaixu1)+' where gupiaoname =\''+ list[0]+'\'')
            # cur.execute('insert into gupiaoinfo(gupiaoname,gupiaono,latestlowprice,latesthighprice,longlowprice,price,jiazhipaixu,fengxianpaixu) values(\''+list[0]+'\',\''+list[1]+'\',\''+list[3]+'\',\''+list[2]+'\',\''+list[5]+'\',\''+list[4]+'\',\''+str(jiazhipaixu1)+'\',\''+str(fengxianpaixu1)+'\')')
            conn.commit();
            cur.close()#关闭游标
            conn.close()#释放数据库资源
        except  Exception:
            raise
print('ok!!!!!!!!!!!!!!!!!')