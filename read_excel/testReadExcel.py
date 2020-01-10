# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 10:17 下午
# @Author  : Silver
# @File    : testReadExcel.py
# @Project_name:
import openpyxl
from openpyxl import workbook
rd = openpyxl.load_workbook('../data/登陆接口测试用例.xlsx')
a = rd['Sheet1']
print(a)