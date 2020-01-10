# -*- coding: utf-8 -*-
# @Time    : 2020/1/4 8:57 上午
# @Author  : Silver
# @File    : test1.py
# @Project_name:
#调用接口
import requests

# resp=requests.get(url,data.yaml)
# print(resp.text)
#定义一个get方法

class Ruquest_Class():

    def get_method(self,url,data=None):
        return requests.get(url,data)

    #定义一个post方法
    def post_method(self,url,data):
        return requests.post(url,data)

    #判断请求方法是get还是post
    def get_or_post(self,method,url,data):
        if method == 'GET':
            return  self.get_method(url,data)
        elif method == 'POST':
            return self.post_method(url,data)
        else:
            raise ValueError
    #定义一个方法，判断返回参数如果是json返回json，如果不是json返回text
    def json_or_text(self,method,url,data):
        try:
            return self.get_or_post(method,url,data).json()
        except:
            return self.get_or_post(method,url,data).text

if __name__ == '__main__':
    url = 'http://127.0.0.1:8888/login/'
    data = {"username": "xiaoqiang", "password": "123"}
    response = Ruquest_Class()
    #resp=response.json_or_text('POST',url,data.yaml)
    print(response.json_or_text('POST',url,data))
    print(response.json_or_text('GET', url, data))


