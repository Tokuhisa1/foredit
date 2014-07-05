def your_mind():
    print "1.input staff info(ISI)\n2.list staff info(LSI)\n3.delte info(DI)\n4.help(H)\n5.quit(Q)\n"
    min=raw_input("INPUT:")
    min=min.strip()
    return min

def main():
        while True:
		      cmd=your_mind()
		      if cmd=='ISI':
			      print "one ok"
		      elif cmd=='LSI':
		              print "two ok"
		      elif cmd=="DI":
		              print "three ok"
		      elif cmd=="H":
		              print "help ok"
		      elif cmd=="Q":
			      print "quit ok"
		      else:
			      print "please input ISI,LSI,DI,H,Q"

if __name__ == '__main__': main()