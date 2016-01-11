#!/usr/local/bin/python3
#coding=utf-8

import urllib.request
import re

gupiaolists = []
gupiaolists2 = []
gupiaolists3 = []

f= urllib.request.urlopen('http://hq.gucheng.com/gpdmylb.html')
content = f.read().decode('gb2312')

pattern = re.compile('\w{8}>.*?\(\d{6}\)')
items = re.findall(pattern,content)
for item in items:
    gupiaolists.append(item.split('>'))

for gupiaolist in gupiaolists:
    # print(gupiaolist[1])
    gupiaolists2.append(gupiaolist[1].split('('))
    gupiaolists3.append(gupiaolist[0].split('('))


