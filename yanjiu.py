#!/usr/bin/python
#coding=utf-8

import poplib
import cStringIO
import email
import email.Header
import base64,os,sys,re
import time
import datetime

#POP3取信
M = poplib.POP3('pop3.163.com')   #邮件下载服务器
M.user('18829210056')    #邮箱地址
M.pass_('wyh123')   #密码

num = len(M.list()[1])
print "the mail sum",num,"jian"
ret = M.list()
print ret
# 取第一封邮件完整信息，在返回值里，是按行存储在down[1]的列表里的。down[0]是返回的状态信息
hdr,message,octet=M.retr(3)
print type(M.retr(1))
print type(hdr)
print message
print type(octet)
print 
