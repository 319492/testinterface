# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 11:00 下午
# @Author  : Silver
# @File    : send_req_email.py
# @Project_name:

import smtplib
#构建文本
from email.mime.text import MIMEText
#构建带附件
from email.mime.multipart import MIMEMultipart

class Send_email():
    def __init__(self):
        self.host_name = "smtp.163.com"
        self.username = "xliyin6@163.com"
        self.password = "silver840401"
        self.fromuser = "xliyin6@163.com"
        self.touser = "xliyin6@163.com"
    #构建一个邮件（组成：收件人、发件人、邮件标题、正文、附件）
    def creat_email(self):
        #获取构建附件的对象
        massage = MIMEMultipart()
        massage['Subject']="接口自动化测试报告"
        massage['From']=self.fromuser
        massage['To']=self.touser
        # 添加正文
        get_data = MIMEText("接口用例共？条，执行？条，通过？条，失败？条",_subtype="plain",_charset="utf-8")
        massage.attach(get_data)
        return massage
    #声明一个邮件服务
    def crear_server(self):
        get_smtp=smtplib.SMTP()
        #先建立连接
        get_smtp.connect(self.host_name)
        #登陆邮箱
        get_smtp.login(self.username,self.password)
        #发送邮件以str形式发送
        get_smtp.sendmail(self.fromuser,self.touser,self.creat_email().as_string())

if __name__ == '__main__':
    send = Send_email()
    send.crear_server()




