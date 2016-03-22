#-*- coding=utf-8 -*-
import os.path

rootdir = '/root/gupiao/data/'


for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
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
                # maxlist.append(0.0)
                continue
            if(tmp[3] != '' and float(tmp[3]) != 0):
                minlist.append(float(tmp[3]))
            else:
                # minlist.append(0.0)
                continue
            pricelist.append(tmp[4])
        f.close()
        #排序
        maxlist.sort(reverse= True)
        minlist.sort(reverse= False)

        if(maxlist and minlist):
            f2 = open('/root/gupiao/result/'+filename,'w')
            f2.write(namelist[0]+'#'+nolist[0]+'#'+str(maxlist[0])+'#'+str(minlist[0])+'#'+pricelist[-1])
            f2.close()

        # print(maxlist,minlist,pricelist)