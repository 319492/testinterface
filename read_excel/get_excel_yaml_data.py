# -*- coding: utf-8 -*-
# @Time    : 2020/1/6 3:19 下午
# @Author  : Silver
# @File    : get_excel_yaml_data.py
# @Project_name:
from read_excel import Excel_Const
from read_excel.testread_excel import Read_Excle
import yaml
class Get_Param():
    #获取excel中的列
    def get_case_param(self):
        return int(Excel_Const.get_case_input())

    #获取excel中的单元格
    def get_cell_param(self,sheet_name,row,case_path):
        return Read_Excle().get_excel_data(sheet_name,row,self.get_case_param(),case_path)

    #通过单元格中的参数调用yaml中的参数
    def get_yaml_data(self,sheet_name,row,case_path,yam_path):
        with open(yam_path) as fp:
            get_obj = yaml.safe_load(fp)
            return get_obj[self.get_cell_param(sheet_name,row,case_path)]

# if __name__ == '__main__':
#     get = Get_Param()
#     get1 = get.get_yaml_data("Sheet1",3)
#     print(get1)

# from read_excel.testread_excel import Read_Excle
# from read_excel import Excel_Const
# get_param = int(Excel_Const.get_case_input())
# rd = Read_Excle()
# get_data=rd.get_excel_data("Sheet1",3,get_param)
#
# with open("../data/data_config.yaml") as fp:
#     get = yaml.load(fp,yaml.Loader)
#     print(get[get_data])









