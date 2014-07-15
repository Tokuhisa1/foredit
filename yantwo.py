# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 09:07:11 2014

@author: wyh
"""

#!/usr/bin/python
#coding=utf-8

import poplib
#coding:utf-8
import cStringIO
import email
import email.Header
#POP3取信
M = poplib.POP3('pop3.163.com')   #邮件下载服务器
M.user('18829210056')    #邮箱地址
M.pass_('wyh123')   #密码
#打印有多少封信
num = len(M.list()[1])
m = M.retr(num)
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
mingling=unicode(subject,subcode)
line=mingling
#print mingling
m_start=line.find("##")    
m_start=m_start+2
if m_start>0: 
      print m_start
      m_end=line.find("##",2)
      if m_end>0:
       print m_end
       print line[m_start:m_end]
      else:
       print "error"
else:
      print "No command now"       

M.quit()
print 'exit'

