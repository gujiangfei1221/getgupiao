#!/usr/local/bin/python3
#coding=utf-8

import urllib.request
import re

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
    # print(gupiaolist[1].split('('))
    gupiaolists2.append(gupiaolist[1].split('('))
    gupiaonolist.append(gupiaolist[0])

for gupiaolist2 in gupiaolists2:
    gupiaonamelist.append(gupiaolist2[0])

# print(gupiaolists)
# print(gupiaonamelist)
# print(gupiaonolist)

nvs = zip(gupiaonolist,gupiaonamelist)
nvDict = dict( (name,value) for name,value in nvs)

print(nvDict)

