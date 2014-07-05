#-*- coding:UTF-8 -*-
'''
======================================
????? http://www.oschina.net/code/snippet_148170_10661 ????
Adapted BY: bepcao
Mail:peterc9511@gmail.com
======================================
'''
from sgmllib import SGMLParser
import sys,urllib2,urllib,cookielib
import datetime
import time
class spider(SGMLParser):
    def __init__(self,email,password):
        SGMLParser.__init__(self)
        self.h3=False
        self.h3_is_ready=False
        self.div=False
        self.h3_and_div=False
        self.a=False
        self.depth=0
        self.names=""
        self.dic={}   
         
        self.email=email
        self.password=password
        self.domain='renren.com'
        try:
            cookie=cookielib.CookieJar()
            cookieProc=urllib2.HTTPCookieProcessor(cookie)
        except:
            raise
        else:
            opener=urllib2.build_opener(cookieProc)
            urllib2.install_opener(opener)       

    def login(self):
        print 'start'
        url='http://www.renren.com/PLogin.do'
        postdata={
                  'email':self.email,
                  'password':self.password,
                  'domain':self.domain  
                  }
        req=urllib2.Request(
                            url,
                            urllib.urlencode(postdata)            
                            )
        
        self.file=urllib2.urlopen(req).read()
        idPos=self.file.index("'id':'")
        self.id=self.file[idPos+6:idPos+15]
        tokPos=self.file.index("get_check:'")
        self.tok=self.file[tokPos+11:tokPos+21]
        rtkPos=self.file.index("get_check_x:'")
        self.rtk=self.file[rtkPos+13:rtkPos+21]
    


    def publish(self,content):
        url1='http://shell.renren.com/'+self.id+'/status'
        postdata={
                  'content':content,
                  'hostid':self.id,
                  'requestToken':self.tok,
                  '_rtk':self.rtk,
                  'channel':'renren',
                  }
        req1=urllib2.Request(
                            url1,
                            urllib.urlencode(postdata)            
                            )
        self.file1=urllib2.urlopen(req1).read()
        print '%s:\nzhuangtai %s fale\nneirong:(%s)'% (datetime.datetime.now(),self.email,postdata.get('content',''))



renrenspider=spider('919936973@qq.com','qimengyuan')
renrenspider.login()
content=raw_input('shuru:')
renrenspider.publish(content)