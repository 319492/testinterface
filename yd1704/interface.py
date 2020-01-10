# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 8:26 下午
# @Author  : Silver
# @File    : interface.py
# @Project_name:
import requests
import json
#模拟发送请求
# url = 'http://127.0.0.1:8888/login/'
# data.yaml = {"username":"silver","password":"123456"}
# #发送get请求
class Request_Class():
    def get_method(self,url,data=None):
        get_response=requests.get(url,data)
        return get_response.text
    #发送post请求
    def post_method(self,url,data):
        get_response=requests.post(url,data)
        return get_response.text
    #判断请求方法
    def get_or_post(self,method,url,data):
        if method=='GET':
            return self.get_method(url,data)
        elif method=='POST':
            return self.post_method(url,data)
        else:
            raise ValueError
if __name__ == '__main__':
    url = 'http://127.0.0.1:8888/login/'
    data = {"username": "silver", "password": "123456"}
    a=Request_Class
    print(a.get_or_post("POST",url,data))