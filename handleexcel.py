# -*- coding=utf-8 -*-

import xlrd, pymysql


def open_excel(file='/Users/gujiangfei/Desktop/模板.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(e.args)


# 根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file='/Users/gujiangfei/Desktop/模板.xlsx', colnameindex=0, by_index=0):
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
            f = open('data/' + (row['股票名称'] + row['股票代码']) + '.txt', 'a')
            f.write(str(row['股票名称']) + "#" + str(row['股票代码']) + "#" + str(row['短期最高价']) + "#" + str(row['短期最低价']) + "#" + '0')
            f.write('\n')
            f.close()

            f2 = open('data2/' + (row['股票名称'] + row['股票代码']) + '.txt', 'a')
            f2.write(str(row['股票名称']) + "#" + str(row['股票代码']) + "#" + str(row['长期最低价']))
            f2.write('\n')
            f2.close()
    print('ok!!!!!!!!!!!!!!!!')

if __name__ == "__main__":
    main()
