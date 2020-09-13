# *_*coding:utf-8 *_*
import smtplib
from email.mime.text import MIMEText
import os
with open('out.txt','r',encoding='utf-8') as f:
    message = f.read()
f.close()
msg = MIMEText(message, 'plain', 'utf-8')
# 发送邮箱地址
from_addr = ''
# 邮箱授权码，非登陆密码
password = ''
# 收件箱地址
to_addr = ''
# smtp服务器
smtp_server = 'smtp.qq.com'
# 发送邮箱地址
msg['From'] = "autoresign"
# 收件箱地址
msg['To'] = ""
# 主题
msg['Subject'] = 'DailyReport'

server = smtplib.SMTP_SSL(smtp_server, 465)
# 假如不是阿里的话
# server = smtplib.SMTP(smtp_server, 25)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
os.remove('out.txt')
