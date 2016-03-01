#!/usr/local/bin/python3
#-*- coding=utf-8 -*-

import os, io, sys, re, time, json, base64
import webbrowser, urllib.request

ChinaStockIndividualList = [
    'sz002310','sz000713'
]

day = 3


#国内股票数据：个股
def getChinaStockIndividualInfo(stockCode,day):
    try:
        #exchange = "sh" if (int(stockCode) // 100000 == 6) else "sz"
        dataUrl = "http://hq.sinajs.cn/list=" + stockCode
        stdout = urllib.request.urlopen(dataUrl)
        stdoutInfo = stdout.read().decode('gb2312')
        tempData = re.search('''(")(.+)(")''', stdoutInfo).group(2)
        stockInfo = tempData.split(",")
        #stockCode = stockCode,
        stockName   = stockInfo[0]  #名称
        #stockStart  = stockInfo[1]  #开盘
        #stockLastEnd= stockInfo[2]  #昨收盘
        stockCur    = stockInfo[3]  #当前
        stockMax    = stockInfo[4]  #最高
        stockMin    = stockInfo[5]  #最低
        #stockUp     = round(float(stockCur) - float(stockLastEnd), 2)       #涨跌
        #stockRange  = round(float(stockUp) / float(stockLastEnd), 4) * 100  #幅度
        #stockVolume = round(float(stockInfo[8]) / (100 * 10000), 2)         #总手
        #stockMoney  = round(float(stockInfo[9]) / (100000000), 2)           #金额
        #stockTime   = stockInfo[31]                                         #更新时间

        # content = "#" + stockName + "#(" + stockCode + ")" + " 开盘:" + stockStart \
        # + ",最新:" + stockCur + ",最高:" + stockMax + ",最低:" + stockMin \
        # + ",涨跌:" + str(stockUp) + ",幅度:" + str(stockRange) + "%" \
        # + ",总手:" + str(stockVolume) + "万" + ",金额:" + str(stockMoney) \
        # + "亿" + ",更新时间:" + stockTime + "  "

        if(os.path.exists('data/'+(stockName+stockCode)+'.txt')):
            f = open('data/'+(stockName+stockCode)+'.txt','r+')
            line = f.readlines()
            num = len(line)
            # print(num)
            if(num > day):
                for i in range(0,num - day):
                    line.pop(i)
            f.close()
            f2 = open('data/'+(stockName+stockCode)+'.txt','w')
            for i in line:
                f2.writelines(i)
            f2.close()

        f3 = open('data/'+(stockName+stockCode)+'.txt','a+')
        f3.write(stockMax + "#" + stockMin + "#" + stockCur)
        f3.write('\n')
        f3.close()



        #content =  stockName + "#" + stockCode + "#" + stockMax + "#" + stockMin + "#" + stockCur

        #twitter = {'message': content}

    except Exception as e:
        print(">>>>>> Exception: " + str(e))
    else:
        return
    finally:
        None

def test_china_individual_data():
    for stockCode in ChinaStockIndividualList:
        getChinaStockIndividualInfo(stockCode,day)

#主函数
def main():
    "main function"
    test_china_individual_data()

if __name__ == '__main__':
    main()