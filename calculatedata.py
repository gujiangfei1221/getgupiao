#-*- coding=utf-8 -*-
import os.path

rootdir = 'data/'


for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        maxlist = []
        minlist = []
        pricelist = []
        f = open('data/'+filename,'r+')
        for i in f.readlines():
            tmp = i.split('#')
            maxlist.append(tmp[0])
            minlist.append(tmp[1])
            pricelist.append(tmp[2])
        f.close()

        #排序
        maxlist.sort()
        minlist.sort()
        pricelist.sort()

        f2 = open('result/'+filename,'w')
        f2.write(maxlist[0]+'#'+minlist[0]+'#'+pricelist[0])
        f2.close()
        # print(maxlist,minlist,pricelist)