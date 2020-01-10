# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 9:44 上午
# @Author  : Silver
# @File    : run_request.py
# @Project_name:
from yd1704.RequestTest import Request_Class
from read_excel import Excel_Const
from read_excel.get_excel_yaml_data import Get_Param
from read_excel.testread_excel import Read_Excle
from read_excel.write_excel import writeExcel

#封装方法
class run_req():
    #获取url
    def get_url(self):
        return int(Excel_Const.get_case_url())

    #获取method
    def get_method(self):
        return int(Excel_Const.get_case_method())

    #获取act
    def get_act(self):
        return int(Excel_Const.get_case_act())

    #获取预期结果
    def get_case_out(self):
        return int(Excel_Const.get_case_out())

    #获取实际结果
    def get_case_res(self):
        return int(Excel_Const.get_case_res())

    #获取用例是否通过
    def get_case_pass(self):
        return int(Excel_Const.get_case_pass())

    #运行接口测试
    def run_request(self,sheet_name,case_path):
        #获取sheet页的所有行å
        hang = Read_Excle().get_excel_row(sheet_name,case_path)
        for row in range(2,hang+1):
            #获取url的值
            url_data = Read_Excle().get_excel_data(sheet_name,row,self.get_url(),case_path)
            #获取method的值
            method_data = Read_Excle().get_excel_data(sheet_name,row,self.get_method(),case_path)
            #获取data单元格
            data = Get_Param().get_yaml_data(sheet_name,row,case_path,"../data/data_config.yaml")
            # 获取act参数单元格
            act = Read_Excle().get_excel_data(sheet_name,row,self.get_act(),case_path)
            #获取预期结果值单元格
            case_out = Read_Excle().get_excel_data(sheet_name,row,self.get_case_out(),case_path)
            #获取实际结果单元格
            resp1 = Read_Excle().get_excel(sheet_name,row,self.get_case_res(),case_path)
            #获取是否通过单元格
            pass_or_no = Read_Excle().get_excel(sheet_name,row,self.get_case_pass(),case_path)
            #判断用例是否执行
            if act == 'Y':
            #调用请求方法
                rq = Request_Class()
                resp = rq.resp_json_or_text(url_data,method_data,data)
                #将返回结果写入excel
                a = writeExcel()
                a.write_old_excel(case_path,row,self.get_case_res(),str(resp))
                #判断预期结果与实际结果是否一致
                if case_out in str(resp) or case_out == str(resp):
                    a = writeExcel()
                    a.write_old_excel(case_path, row, self.get_case_pass(),"测试通过")

                else:
                    a = writeExcel()
                    a.write_old_excel(case_path, row, self.get_case_pass(), "测试失败")


if __name__ == '__main__':
    a = run_req()
    a.run_request("Sheet1","../data/登陆接口测试用例的副本(1).xlsx")
