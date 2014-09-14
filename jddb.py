import sqlite3
conn=sqlite3.connect("/home/wyh/tt.db")
conn.cursor()
#conn.execute("create table mytable (id,num);")
conn.execute("insert into mytable values(123,456)")

conn.commit()
conn.close()
