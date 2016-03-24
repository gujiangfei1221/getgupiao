#-*- coding=utf-8 -*-
import os.path,time

rootdir = '/root/gupiao/data2/'


for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        namelist = []
        nolist = []
        minlist = []
        f = open('/root/gupiao/data2/'+filename,'r+')
        for i in f.readlines():
            tmp = i.split('#')
            namelist.append(tmp[0])
            nolist.append(tmp[1])
            if(tmp[2].strip() != '' and float(tmp[2].strip()) != 0):
                minlist.append(float(tmp[2].strip()))
            else:
                # minlist.append(0.0)
                continue
        f.close()

        #排序
        minlist.sort()

        if(minlist):
            f2 = open('/root/gupiao/result2/'+filename,'w')
            f2.write(str(minlist[0]) + '#' + time.strftime("%Y-%m-%d", time.localtime()))
            f2.close()
        # print(maxlist,minlist,pricelist)