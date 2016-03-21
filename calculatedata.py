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
            if(tmp[2] != ''):
                maxlist.append(float(tmp[2]))
            else:
                # maxlist.append(0.0)
                continue
            if(tmp[3] != ''):
                minlist.append(float(tmp[3]))
            else:
                # minlist.append(0.0)
                continue
            pricelist.append(tmp[4])
        f.close()
        #排序
        maxlist.sort(reverse= True)
        minlist.sort(reverse= False)

        f2 = open('result/'+filename,'w')
        f2.write(namelist[0]+'#'+nolist[0]+'#'+str(maxlist[0])+'#'+str(minlist[0])+'#'+pricelist[-1])
        f2.close()
        # print(maxlist,minlist,pricelist)