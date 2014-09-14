from sys import argv 
from os.path import exists

script,from_file,to_file=argv
print "copying from %s to %s "%(from_file,to_file)
input=open(from_file)
indata=input.read()
print "the input is %d bytes long"%len(indata)
print "Does the output file exist? %r"%exists(to_file)

raw_input("that really?")

output=open(to_file,'w')
output.write(indata)

print "Alright all done"

output.close()
input.close()
