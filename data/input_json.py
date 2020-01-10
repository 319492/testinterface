# -*- coding: utf-8 -*-
# @Time    : 2020/1/6 10:34 下午
# @Author  : Silver
# @File    : input_json.py
# @Project_name:
import json
#将json格式参数写入json文件
# dict1 = {"login":{"username":"zhangsan","password":"123456"}}
# with open("sava.json",mode="w") as fp:
#     #indent是json格式转化属性
#     json.dump(dict1,fp,indent=2)

#读取：字节码流的读取方式
with open("data1.json",mode="rb") as fp:
    get_json = json.load(fp)
    print(get_json)
    print(json.dumps(get_json,indent=4))