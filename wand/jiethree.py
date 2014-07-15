# -*- coding: utf-8 -*-

import poplib
from email import parser

host = 'pop.163.com'
username = '18829210056'
password = 'wyh123'

pop_conn = poplib.POP3_SSL(host)
pop_conn.user(username)
pop_conn.pass_(password)

#Get messages from server:
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]

# Concat message pieces:
messages = ["\n".join(mssg[1]) for mssg in messages]

#Parse message intom an email object:
messages = [parser.Parser().parsestr(mssg) for mssg in messages]
for message in messages:
    print message['Subject']
pop_conn.quit()

def showMessage(mail):
    if mail.is_multipart():
        for part in mail.walk():
              showmessage(part)
    else:
        type=mail.get_content_charset()
        if type=='None':
            print mail.get_payload()
        else:
            try:
              print unicode(mail.get_payload('base64'),type)
            except:
              print mail.get_payload()

for id in range (numMsgs):
    hdr,message,octet=popClient.retr(id+1)
    mail=email.message_from_string(string.join(message,'\n'))
    mail['subject'],mail.get('subject')
    mail['from'],mail.get('from')
    mail['To'],mail.get('To')
    mail['date'],mail.get('date')
    subject = email.Header.decode_header(mail['subject'])[0][0]
    subcode=  email.Header.decode_header(mail['subject'])[0][1]
    FromAddr=email.Header.decode_header(mail['from'])[0][0]
    ToAddr=email.Header.decode_header(mail['To'])[0][0]
    date=email.Header.decode_header(mail['date'])[0][0]
    print '*******************************************'
    print '   ********** mail',id+1,'****************   '
    print '\n'
    print  'Subject: ',subject
    print 'From: ',FromAddr
    print 'To: ',ToAddr
    print 'Date: ',date
    print '????:'
    showMessage(mail)
    print '\n\n'
    
popClient.quit()
