from sys import argv
script,filename=argv
file=open(filename)
print "open %r"%filename
for line in file:
    m_start=line.find("0273")
    m_end=line.find("986")
    if m_start>0: 
      m_start=m_start+4
      print m_start
    if m_end>0:
      print m_end
      print line[m_start:m_end]
   
