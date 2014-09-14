#!/usr/bin/python
#coding=utf-8

import poplib
#coding:utf-8
import cStringIO
import email
import email.Header
import base64,os,sys,re
import time
import datetime


yesterday=time.strftime("%Y/%m/%d",time.localtime(time.time()-24*60*60))
yesterday1=time.strftime("%Y%m%d",time.localtime(time.time()-24*60*60))
#sub="Fwd: %s - D10 - Daily Details Report & Statement" % (yesterday)
#sub="%s *- *D10 *- *Daily *Details *Report *& *Statement" % (yesterday)
sub="中文"   #匹配字符
print sub
wd = '/tmp'
f1 = wd+"/"+yesterday1+"_D10_UK_Details.xls"
os.chdir(wd)     # 切换工作目录，附件会存在这个目录下面。

if os.path.isfile(f1):                 #判断附件是否已经下载过了，是：退出程序；否：继续。
        print "file is existed..."
        sys.exit()

#POP3取信
M = poplib.POP3('pop3.163.com')   #邮件下载服务器
M.user('18829210056')    #邮箱地址
M.pass_('wyh123')   #密码
#打印有多少封信
num = len(M.list()[1])
print 'num of messages', num
if num >= 5:
        num1 = num-5
else:
        num1 = 0

#for i in range(numMessages):
for i in range(num,num1,-1):
    #m = M.retr(i+1)
    m = M.retr(i)

    buf = cStringIO.StringIO()
    for j in m[1]:
        print >>buf, j
    buf.seek(0)
    #解析信件内容
    msg = email.message_from_file(buf)
    subject = msg.get("subject") # 取信件头里的subject,　也就是主题
    # 下面的三行代码只是为了解码象=?gbk?Q?=CF=E0=C6=AC?=这样的subject
    h = email.Header.Header(subject)
    dh = email.Header.decode_header(h)
    subcode = dh[0][1]
    subject = dh[0][0]
    if not subcode :
        subcode = 'utf-8'
    print "subcode",subcode
    print "subject:", unicode(subject,subcode)

M.quit()
print 'exit'

