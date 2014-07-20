import httplib
conn = httplib.HTTPConnection("192.168.2.105")
conn.request('get', '/')
print conn.getresponse().read()
conn.close()