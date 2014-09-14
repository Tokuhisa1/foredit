from sys import argv
script,filename=argv
test=open(filename)
print "open %r"%filename
print test.read()