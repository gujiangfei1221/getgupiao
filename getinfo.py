#!/usr/local/bin/python3
#-*- coding=utf-8 -*-

import os, io, sys, re, time, json, base64
import webbrowser, urllib.request

ChinaStockIndividualList = [
    "000063", #  中兴通讯
    "600036", #  招商银行
]

#国内股票数据：个股
def getChinaStockIndividualInfo(stockCode):
    try:
        exchange = "sh" if (int(stockCode) // 100000 == 6) else "sz"
        dataUrl = "http://hq.sinajs.cn/list=" + exchange + stockCode
        stdout = urllib.request.urlopen(dataUrl)
        stdoutInfo = stdout.read().decode('gb2312')
        tempData = re.search('''(")(.+)(")''', stdoutInfo).group(2)
        stockInfo = tempData.split(",")
        #stockCode = stockCode,
        stockName   = stockInfo[0]  #名称
        stockStart  = stockInfo[1]  #开盘
        stockLastEnd= stockInfo[2]  #昨收盘
        stockCur    = stockInfo[3]  #当前
        stockMax    = stockInfo[4]  #最高
        stockMin    = stockInfo[5]  #最低
        stockUp     = round(float(stockCur) - float(stockLastEnd), 2)
        stockRange  = round(float(stockUp) / float(stockLastEnd), 4) * 100
        stockVolume = round(float(stockInfo[8]) / (100 * 10000), 2)
        stockMoney  = round(float(stockInfo[9]) / (100000000), 2)
        stockTime   = stockInfo[31]

        content = "#" + stockName + "#(" + stockCode + ")" + " 开盘:" + stockStart \
        + ",最新:" + stockCur + ",最高:" + stockMax + ",最低:" + stockMin \
        + ",涨跌:" + str(stockUp) + ",幅度:" + str(stockRange) + "%" \
        + ",总手:" + str(stockVolume) + "万" + ",金额:" + str(stockMoney) \
        + "亿" + ",更新时间:" + stockTime + "  "

        twitter = {'message': content}

    except Exception as e:
        print(">>>>>> Exception: " + str(e))
    else:
        return twitter
    finally:
        None

def test_china_individual_data():
    for stockCode in ChinaStockIndividualList:
        twitter = getChinaStockIndividualInfo(stockCode)
        print(twitter['message'])

#主函数
def main():
    "main function"
    test_china_individual_data()

if __name__ == '__main__':
    main()