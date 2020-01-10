# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 9:50 下午
# @Author  : Silver
# @File    : RequestTest.py
# @Project_name:
import requests
#模拟接口发送请求
# url='http://127.0.0.1:8888/login/'
# data.yaml={"username":"zhangsan","password":"12123"}
# get_resp=requests.request(url=url,method='POST',data.yaml=data.yaml)
# print(get_resp.text)
class Request_Class():

    def get_method(self,url,method,data):

        #get_resp = requests.request(url,method,data.yaml)
        get_resp = requests.get(url,data)
        #print(type(get_resp.text))
        return get_resp

    def post_method(self,url,method,data):
        #get_resp = requests.request(url, method, data.yaml)
        get_resp = requests.post(url,data)
        #print(type(get_resp.text))
        return get_resp

    def get_or_post(self,url,method,data):
        if method=='GET':
            return self.get_method(url,method,data)
        elif method=='POST':
            return self.post_method(url,method,data)
        else:
            raise ValueError
    #定义一个方法，判断返回类型是否符合json，符合返回json，不符合返回text
    def resp_json_or_text(self,url,method,data):
        try:
            get_json=self.get_or_post(url,method,data).json()
            return get_json
        except:
            get_text=self.get_or_post(url,method,data).text
            return get_text
#
# if __name__ == '__main__':
#     url = 'http://127.0.0.1:8888/login/'
#     data={"username":"zhangsan","password":"123456"}
#     get_res=Request_Class()
#     # print(get_res.get_or_post(url,"POST",data.yaml))
#     print(get_res.resp_json_or_text(url, "GET", data))
#     print(get_res.resp_json_or_text(url, "POST", data))
#     # print(get_res.resp_json_or_text(url, "PUT", data.yaml))







