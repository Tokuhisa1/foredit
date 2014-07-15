import sys,string,sqlite3,webbrowser

def your_mind():
    print "************************************************"
    print "1.input staff info(INSI)\n2.list staff info(LSI)\n3.delte info(DI)\n4.help(H)\n5.quit(Q)\n"
    print "************************************************"
    min=raw_input(">>")
    min=min.strip()
    return min

def your_input():
	print "please input your staff info in turn\n"
	st_id=raw_input("please input id")	
	st_id=string.atoi(st_id)
        st_name=raw_input("please input name")
	st_age=raw_input("please input age")
	st_age=string.atoi(st_age)
	st_sex=raw_input("please input sex")
	st_sex=string.atoi(st_sex)
	st_level=raw_input("please input level")
	st_level=string.atoi(st_level)
	st_last=raw_input("please input other things")
        conn=sqlite3.connect("goddess.db")
        conn.cursor()
        #conn.execute("create table mytable (id,num);")
        conn.execute("insert into staff values(%r,%r,%r,%r,%r,%r)"%(st_id,st_name,st_age,st_sex,st_level,st_last))
	conn.commit()
        conn.close()
def your_list():
	print "what do you want to see\n1.all(A)\n2.id(I)\n3.name(N)\n4.level(L)\n"
	lc=raw_input(">>")
	lc=lc.strip()
	if lc=='A':
		print "A"
		conn=sqlite3.connect("goddess.db")
                conn.cursor()
		st_all=conn.execute("select * from staff")
		for eye in st_all:
			print eye
		conn.commit()
		conn.close()
	elif lc=="I":
	        print "I"
		conn=sqlite3.connect("goddess.db")
                conn.cursor()
                #conn.execute("create table mytable (id,num);")
		st_id=conn.execute("select id from staff;")
                for eye in st_id:
			print eye
		conn.commit()
		conn.close()
	elif lc=="N":
	        print "N"
		conn=sqlite3.connect("goddess.db")
                conn.cursor()
                #conn.execute("create table mytable (id,num);")
		st_name=conn.execute("select name from staff;")
		for eye in st_name:
			print eye
		conn.commit()
		conn.close()
	elif lc=="L":
		print "L"
		conn=sqlite3.connect("goddess.db")
                conn.cursor()
                #conn.execute("create table mytable (id,num);")
		st_level=conn.execute("select level from staff;")
		for eye in st_level:
			print eye
		conn.commit()
		conn.close()
	else:
		print "please input A I N L"
		
	
		
def your_delete():
	print "what do you want to delete\n1.id(I)\n2.name(N)\n"
	lc=raw_input(">>")
	lc=lc.strip()
	if lc=="I":
	    print "I"
	    print "please input id"
	    ss_id=raw_input(">>")
	    ss_id=string.atoi(ss_id)
	    conn=sqlite3.connect("goddess.db")
            conn.cursor()
            #conn.execute("create table mytable (id,num);")
            conn.execute("delete from staff where id=%r;"%ss_id)
	    conn.commit()
            conn.close()
	elif lc=="N":
	    print "N"
	    print "please input id"
	    ss_name=raw_input(">>")
	    conn=sqlite3.connect("goddess.db")
            conn.cursor()
            #conn.execute("create table mytable (id,num);")
            conn.execute("delete from staff where id=%r;"%ss_name)
	    conn.commit()
            conn.close()
	else:
		print "please input I N " 
		
	
       	
	
def main():
        while True:
		      cmd=your_mind()
		      if cmd=='INSI':
			      print "one ok"
			      cmd_two=your_input()
		      elif cmd=='LSI':
		              print "two ok"
			      cmd_three=your_list()
		      elif cmd=="DI":
		              print "three ok"
			      cmd_four=your_delete()
		      elif cmd=="H":
		              print "help ok"
			      webbrowser.open_new_tab('http://www.baidu.com')		      
		      elif cmd=="Q":
			      print "quit ok"
			      sys.exit()
		      else:
			      print "please input ISI,LSI,DI,H,Q"

if __name__ == '__main__': main()

