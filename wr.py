from  sys import argv
script,filename=argv

print "Well you are going to erase %r"%filename
print "if you dont want that, hit ctrl-c"
print "if you do want that return"

raw_input("?")

print "Opening the file..."
target=open(filename,'w')
print "saygoodbye"
target.truncate()

print "Now im ask you for three lines"
 
line1=raw_input("line1: ")
line2=raw_input("line2: ")
line3=raw_input("line3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally we close it"
target.close()
