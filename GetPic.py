import pandas as pd
import requests


def get_pic(n):
    xls = pd.ExcelFile(r'表格\testtabl.xls')
    xls2 = pd.read_excel(xls, 'testtabl', usecols=['ID','WordWB'])
    src_WB = xls2['WordWB'][n]
    ID_WB = xls2['ID'][n]
    return [ID_WB, src_WB]


if __name__ == '__main__':
    for i in range(53,54):
        xls_WB = get_pic(i)
        with open(r"图片\女书图片\%d.jpg"%xls_WB[0], "wb")as file:
            file.write(requests.get(xls_WB[1]).content)
    print("图片保存成功！！")