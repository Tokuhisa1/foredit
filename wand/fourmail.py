#coding:utf-8
import   poplib   
import   cStringIO   
import   email   
import   base64   
    
  #POP3取信   
M   =   poplib.POP3("pop3.163.com")   
M.user("18829210056")   
M.pass_("wyh123")   
    
#打印有多少封信   
numMessages   =   len(M.list()[1])   
print   'num   of   messages',   numMessages   
    
    
for   i   in   range(numMessages):           
          m   =   M.retr(i+1)   
            
          buf   =   cStringIO.StringIO()   
          for   j   in   m[1]:                   
                  print   >>buf,   j   
          buf.seek(0)   
    
          #解析信件内容   
          msg   =   email.message_from_file(buf)   
          for   part   in   msg.walk():   
                  contenttype   =     part.get_content_type()     
                  filename   =   part.get_filename()   
                    
                  if   filename   and   contenttype   ==   'application/octet-stream':   
                          #   保存附件   
                          f   =   open("mail%d.%s.attach"   %   (i+1,filename),'wb')   
                          f.write(base64.decodestring(part.get_payload()))   
                          f.close()   
                  elif   contenttype   ==   'text/plain':   
                          #   保存正文   
                          f   =   open("mail%d.txt"   %   (i+1),'wb')   
                          f.write(base64.decodestring(part.get_payload()))   
                          f.close()  
