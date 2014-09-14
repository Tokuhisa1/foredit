# -*- coding: utf-8 -*-
import urllib2
import urllib
import cookielib
data={"email":"919936973@qq.com","password":"qimengyuan"}#???????
post_data=urllib.urlencode(data )#?data??url??
cj=cookielib.CookieJar()#??cookie??
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))#??cookie???????opener
req=urllib2.Request("http://www.renren.com/PLogin.do",post_data)#????
content=opener.open(req)
print content.read().decode('utf-8')#????
