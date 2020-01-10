# -*- coding: utf-8 -*-
# @Time    : 2020/1/6 10:00 上午
# @Author  : Silver
# @File    : Excel_Const.py
# @Project_name:
class Excel_Const():
    case_id = '1'
    case_mod = '2'
    case_url = '3'
    case_method = '4'
    case_input = '5'
    case_out = '6'
    case_res = '7'
    case_act = '8'
    case_pass = '9'
#定义用例编号
def get_case_id():
    return Excel_Const.case_id

#定义用例模块
def get_case_mod():
    return Excel_Const.case_mod

#定义用例#url
def get_case_url():
    return Excel_Const.case_url

#定义用例方法
def get_case_method():
    return Excel_Const.case_method

#定义用例输入参数
def get_case_input():
    return Excel_Const.case_input

#定义用例预期结果
def get_case_out():
    return Excel_Const.case_out

#定义用例实际结果
def get_case_res():
    return Excel_Const.case_res

#定义用例是否执行
def get_case_act():
    return Excel_Const.case_act

#定义用例是否通过
def get_case_pass():
    return Excel_Const.case_pass