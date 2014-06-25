#!/usr/bin/env python3
#coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '18829210056@163.com'
receiver = '18829210056@163.com'
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = '18829210056'
password = 'wyh123'

msg = MIMEText('i love you','plain','utf-8')#?????'utf-8',????????
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()