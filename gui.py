from Tkinter import *
def Hest():
 print "hellowworld"
app=Tk()
app.title("for goddess text V0.01")
app.geometry('500x300+100+100')
b1=Button(app,text="save",width=10,command=Hest)
b1.pack(side='left',padx=40,pady=50)
b2=Button(app,text="exit",width=10,command=app.quit) #write a exit button use "app.quit"
b2.pack(side='left',padx =40,pady=70)
var=StringVar()
l1=Label(app,textvariable=var,padx=50,pady=200)
var.set("this is a simple text")
l1.pack() 
t1=Text(app,padx=10,pady=10,width=20)
t1.pack()

app.mainloop()
