#-*- coding=utf-8 -*-

import pymysql,time,os,sys

rootdir = 'data/'

def datetrans(tdate):
        spdate = tdate.replace("/","-")
        try:
                datesec = time.strptime(spdate,'%Y-%m-%d')
        except ValueError:
                print("%s is not a rightful date!!" % tdate)
                sys.exit(1)
        return time.mktime(datesec)

def daysdiff(d1,d2):
        daysec = 24 * 60 * 60
        return int(( d1 - d2 )/daysec)

for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        f = open('data/'+filename,'r+')
        for i in f.readlines():
            tmp = i.split('#')
            gupiaono = tmp[1]
            continue

        try:
            #获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
            conn=pymysql.connect(host='localhost',user='root',passwd='root',db='codeigniter',port=8889,charset='utf8')
            cur=conn.cursor()#获取一个游标
            cur.execute('select yichangdate from gupiaoinfo where gupiaono = \'' + 'sh600061' +'\' and yichang = \'' + 'yichang' +'\'')
            r = cur.fetchall()
            if(len(r) > 0):
                date1 = time.strftime("%Y-%m-%d", time.localtime())
                date2 = r[0][0]
                date1sec = datetrans(date1)
                date2sec = datetrans(date2)
                if(daysdiff(date1sec,date2sec) >= 3):
                    cur.execute('update gupiaoinfo set yichang = \'zhengchang\', yichangdate = \''+ time.strftime("%Y-%m-%d", time.localtime()) +'\' where gupiaono = \''+ 'sh600061' +'\'')
                conn.commit();
            cur.close()#关闭游标
            conn.close()#释放数据库资源
        except  Exception as e:
            print(e.args)
