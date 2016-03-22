# -*- coding=utf-8 -*-

import xlrd, pymysql


def open_excel(file='/root/gupiao/模板.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(e.args)


# 根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file='/root/gupiao/模板.xlsx', colnameindex=0, by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数
    colnames = table.row_values(colnameindex)  # 某一行数据
    list = []
    for rownum in range(1, nrows):

        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list


def main():
    tables = excel_table_byindex()
    for row in tables:
        if (row['股票名称'] != ''):
            f = open('/root/gupiao/data/' + (row['股票名称'] + row['股票代码']) + '.txt', 'a')
            f.write(str(row['股票名称']) + "#" + str(row['股票代码']) + "#" + str(row['短期最高价']) + "#" + str(row['短期最低价']) + "#" + '0')
            f.write('\n')
            f.close()

            f2 = open('/root/gupiao/data2/' + (row['股票名称'] + row['股票代码']) + '.txt', 'a')
            f2.write(str(row['股票名称']) + "#" + str(row['股票代码']) + "#" + str(row['长期最低价']))
            f2.write('\n')
            f2.close()
            try:
                #获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
                conn=pymysql.connect(host='localhost',user='root',passwd='ede1954b',db='codeigniter',port=3306,charset='utf8')
                cur=conn.cursor()#获取一个游标
                cur.execute('update gupiaoinfo set zhiding = \'yes\''+' where gupiaoname =\''+ row['股票名称'] +'\'')
                # cur.execute('insert into gupiaoinfo(gupiaoname,gupiaono,latestlowprice,latesthighprice,longlowprice,price,jiazhipaixu,fengxianpaixu) values(\''+list[0]+'\',\''+list[1]+'\',\''+list[3]+'\',\''+list[2]+'\',\''+list[5]+'\',\''+list[4]+'\',\''+str(jiazhipaixu1)+'\',\''+str(fengxianpaixu1)+'\')')
                conn.commit();
                cur.close()#关闭游标
                conn.close()#释放数据库资源
            except  Exception as e:
                print(e.args)
    print('ok!!!!!!!!!!!!!!!!')

if __name__ == "__main__":
    main()
