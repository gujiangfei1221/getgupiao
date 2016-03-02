#-*- coding=utf-8 -*-
import os.path

rootdir = 'data/'


for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        namelist = []
        nolist = []
        maxlist = []
        minlist = []
        pricelist = []
        f = open('data/'+filename,'r+')
        for i in f.readlines():
            tmp = i.split('#')
            namelist.append(tmp[0])
            nolist.append(tmp[1])
            maxlist.append(tmp[2])
            minlist.append(tmp[3])
            pricelist.append(tmp[4])
        f.close()

        #排序
        maxlist.sort(reverse= True)
        minlist.sort()

        f2 = open('result/'+filename,'w')
        f2.write(namelist[0]+'#'+nolist[0]+'#'+maxlist[0]+'#'+minlist[0]+'#'+pricelist[-1])
        f2.close()
        # print(maxlist,minlist,pricelist)