#-*- coding=utf-8 -*-
import os.path,pymysql,time

rootdir = '/root/gupiao/data/'

for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        # print(filename+'\n')
        namelist = []
        nolist = []
        maxlist = []
        minlist = []
        pricelist = []
        f = open('/root/gupiao/data/'+filename,'r+')
        for i in f.readlines():
            tmp = i.split('#')
            namelist.append(tmp[0])
            nolist.append(tmp[1])
            if(tmp[2] != '' and float(tmp[2]) != 0):
                maxlist.append(float(tmp[2]))
            else:
                continue
            if(tmp[3] != '' and float(tmp[3]) != 0):
                minlist.append(float(tmp[3]))
            else:
                continue
            pricelist.append(tmp[4])
        f.close()

        for i in range(0,len(pricelist)-1):
            if(float(pricelist[i]) != 0):
                if(abs((float(pricelist[i]) - float(pricelist[i+1])) / (float(pricelist[i]))) >= 0.11):
                    try:
                        #获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
                        conn=pymysql.connect(host='localhost',user='root',passwd='ede1954b',db='codeigniter',port=3306,charset='utf8')
                        cur=conn.cursor()#获取一个游标
                        cur.execute('update gupiaoinfo set yichang = \'yichang\',yichangdate = \''+ time.strftime("%Y-%m-%d", time.localtime()) +'\' where gupiaoname =\''+ namelist[0]+'\'')
                        # cur.execute('insert into gupiaoinfo(gupiaoname,gupiaono,latestlowprice,latesthighprice,longlowprice,price,jiazhipaixu,fengxianpaixu) values(\''+list[0]+'\',\''+list[1]+'\',\''+list[3]+'\',\''+list[2]+'\',\''+list[5]+'\',\''+list[4]+'\',\''+str(jiazhipaixu1)+'\',\''+str(fengxianpaixu1)+'\')')
                        conn.commit();
                        cur.close()#关闭游标
                        conn.close()#释放数据库资源
                    except  Exception as e:
                        print(e.args)
                else:
                    try:
                        #获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
                        conn=pymysql.connect(host='localhost',user='root',passwd='ede1954b',db='codeigniter',port=3306,charset='utf8')
                        cur=conn.cursor()#获取一个游标
                        cur.execute('update gupiaoinfo set yichang = \'zhengchang\' where gupiaoname =\''+ namelist[0]+'\'')
                        # cur.execute('insert into gupiaoinfo(gupiaoname,gupiaono,latestlowprice,latesthighprice,longlowprice,price,jiazhipaixu,fengxianpaixu) values(\''+list[0]+'\',\''+list[1]+'\',\''+list[3]+'\',\''+list[2]+'\',\''+list[5]+'\',\''+list[4]+'\',\''+str(jiazhipaixu1)+'\',\''+str(fengxianpaixu1)+'\')')
                        conn.commit();
                        cur.close()#关闭游标
                        conn.close()#释放数据库资源
                    except  Exception as e:
                        print(e.args)
            else:
                continue
            print(namelist[0]+'ok!!!!!!!!!!!!')



