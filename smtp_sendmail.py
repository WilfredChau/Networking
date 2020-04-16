"""
引用smtplib库
使用SMTP协议简单发送邮件
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@runoob.com'
receivers = ['wilfredc9623@gmail.com']  # 接收邮件方

# 三个参数：第一个为文本内容，第二个plain设置文本格式，第三个设置编码
message = MIMEText('python邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header('发送', 'utf-8')  # 发送者
message['To'] = Header('接收', 'utf-8')  # 接收者

subject = 'Python SMTP邮件测试'
message['subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('邮箱发送成功')
except smtplib.SMTPException:
    print('Error: 无法发送邮件')



