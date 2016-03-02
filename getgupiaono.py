#!/usr/local/bin/python3
#-*- coding=utf-8 -*-

import urllib.request
import re

def getgupiaono():
    gupiaolists = []
    gupiaolists2 = []
    gupiaonolist = []
    gupiaonamelist = []

    f= urllib.request.urlopen('http://hq.gucheng.com/gpdmylb.html')
    content = f.read().decode('gb2312')

    pattern = re.compile('\w{8}>.*?\(\d{6}\)')
    items = re.findall(pattern,content)
    for item in items:
        gupiaolists.append(item.split('>'))

    for gupiaolist in gupiaolists:
        gupiaolists2.append(gupiaolist[1].split('('))
        gupiaonolist.append(gupiaolist[0])

    for gupiaolist2 in gupiaolists2:
        gupiaonamelist.append(gupiaolist2[0])

    nvs = zip(gupiaonolist,gupiaonamelist)
    nvDict = dict( (name,value) for name,value in nvs)

    tmp = []
    tmp2 = []
    for k,v in nvDict.items():
        if '*' in v:
            continue
        else:
            tmp.append(k)
            tmp2.append(v)
    print(tmp)
    print(tmp2)

    return nvDict

#主函数
def main():
    "main function"
    f = open('gupiao.txt','r+')
    for k,v in getgupiaono().items():
        f.write(k+'#'+v)
        f.write('\r\n')
    f.close()


if __name__ == '__main__':
    main()

