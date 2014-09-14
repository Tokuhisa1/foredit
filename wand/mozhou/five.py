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
    #if subject == sub:
    if re.search(sub,subject):              # 判断主题中是否包含 sub 关键字。
        # 循环信件中的每一个mime的数据块
        for par in msg.walk():
            if not par.is_multipart(): # 这里要判断是否是multipart，是的话，里面的数据是无用的，至于为什么可>以了解mime相关知识。
                name = par.get_param("name") #如果是附件，这里就会取出附件的文件名
                if name:
                #有附件
                # 下面的三行代码只是为了解码象=?gbk?Q?=CF=E0=C6=AC.rar?=这样的文件名
                    h = email.Header.Header(name)
                    dh = email.Header.decode_header(h)
                    fname = dh[0][0]
                    fcode = dh[0][1]
                    if not fcode:
                        fcode = 'utf-8'
                    fname = unicode(fname,fcode)
                    print '附件名:',fname+' fcode:',fcode
                    data = par.get_payload(decode=True) #　解码出附件数据，然后存储到文件中

                    try:
                        f = open(fname, 'wb') #注意一定要用wb来打开文件，因为附件一般都是二进制文件
                    except:
                        print '附件名有非法字符，自动换一个'
                        f = open('aaaa', 'wb')
                    f.write(data)
                    f.close()
                else:
                #不是附件，是文本内容
                    body = par.get_payload(decode=True) # 解码出文本内容，直接输出来就可以了。
                    print 'body:'
                    #print 'body:',body       #中文没有处理好，所有没有输出了。
                print '+'*60 # 用来区别各个部分的输出
    else:
        continue
    print '\n'
M.quit()
print 'exit'

