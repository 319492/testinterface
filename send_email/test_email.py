# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 11:56 下午
# @Author  : Silver
# @File    : test_email.py
# @Project_name:
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

if __name__ == '__main__':
    fromaddr = '137xxxx@163.com'
    password = 'password'
    toaddrs = ['137xxxx@163.com', '137xxxx@qq.com']

    content = 'hello, this is email content.'
    textApart = MIMEText(content)


    imageFile = '1.png'
    imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
    imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)

    pdfFile = '算法设计与分析基础第3版PDF.pdf'
    pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
    pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)

    zipFile = '算法设计与分析基础第3版PDF.zip'
    zipApart = MIMEApplication(open(zipFile, 'rb').read())
    zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

    m = MIMEMultipart()
    m.attach(textApart)
    m.attach(imageApart)
    m.attach(pdfApart)
    m.attach(zipApart)
    m['Subject'] = 'title'

    try:
        server = smtplib.SMTP('smtp.163.com')
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('success')
        server.quit()
    except smtplib.SMTPException as e:
        print('error:', e)  # 打印错误
