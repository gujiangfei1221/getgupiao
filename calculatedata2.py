#-*- coding=utf-8 -*-
import os.path

rootdir = 'data2/'


for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        namelist = []
        nolist = []
        minlist = []
        f = open('data2/'+filename,'r+')
        for i in f.readlines():
            tmp = i.split('#')
            namelist.append(tmp[0])
            nolist.append(tmp[1])
            if(tmp[2].strip() != ''):
                minlist.append(float(tmp[2].strip()))
            else:
                # minlist.append(0.0)
                continue
        f.close()

        #排序
        minlist.sort()

        if(minlist):
            f2 = open('result2/'+filename,'w')
            f2.write(str(minlist[0]))
            f2.close()
        # print(maxlist,minlist,pricelist)