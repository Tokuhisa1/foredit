import sqlite3
from sys import argv
script,filename=argv
test=open(filename)
conn=sqlite3.connect("/home/wyh/tt.db")
print "open %r"%filename
for line in test:
  a,b=line.split(":")
  conn.cursor()
  conn.execute("insert into mytable values(%s,%s)"%(a,b))
  conn.commit()
test.close()
conn.close()
