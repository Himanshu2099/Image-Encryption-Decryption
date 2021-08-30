#######################################################
from decrypt import decryptor
from tkinter import *
import os
from tkinter.filedialog import askopenfilename
decr = Tk()
decr.geometry("510x400")
decr.title("Image Decryption")
decr.resizable(False,False)
#Function Defs
##############################################################
def browsefunc1():
    global filename
    filename=askopenfilename(filetypes=(("PNG Files", "*.png;*.PNG"),("JPEG files", "*.jpg;*.JPG")))
    e1.config(text=filename)
    e1.delete(0,END)
    e1.insert(0,filename)

def browsefunc2():
    global filename
    filename=askopenfilename(filetypes=(("Key file", "*.KEY;*.key"), ))
    e2.config(text=filename)
    e2.delete(0,END)
    e2.insert(0,filename)

def browsefunc3():
    global filename
    filename=askopenfilename(filetypes=(("Key file", "*.KEY;*.key"), ))
    e3.config(text=filename)
    e3.delete(0,END)
    e3.insert(0,filename)

def go_home():
	decr.destroy()
	import main

def start_decrypting():
    global x
    global y 
    global z
    x = e1.get()
    y = e2.get()
    z = e3.get()
    decryptor(x,y,z)

#input Box    
###############################################################
e1=Entry(decr,width=70,borderwidth=1)
e2=Entry(decr,width=70,borderwidth=1)
e3=Entry(decr,width=70,borderwidth=1)
#Button defs
###############################################################
l1 = Label(decr, text = "Location Of File To Decrypt")
l2 = Label(decr, text = "Location Of File Containing the Key 1")
l3 = Label(decr, text = "Location Of File Containing the Key 2")
button_browse1 = Button(decr, text="Browse", command=browsefunc1)
button_browse2 = Button(decr, text="Browse", command=browsefunc2)
button_browse3 = Button(decr, text="Browse",command=browsefunc3)
button_decrypy = Button(decr,text = "Start Decrypting",padx=40,pady=20,command=start_decrypting)
button_back = Button(decr,text = "Go To Home",padx=40,pady=20,command=go_home)

#Button View format
#################################################################
l1.place(x=10,y=30)
button_browse1.place(x=450,y=55)
l2.place(x=10,y=110)
l3.place(x=10,y=198)
button_browse2.place(x=450,y=135)
button_browse3.place(x=450,y=223)
button_back.place(x=50,y=300)
button_decrypy.place(x=270,y=300)
e1.place(x=15,y=60)
e2.place(x=15,y=140)
e3.place(x=15,y=227)





#run
##################################################################
decr.mainloop()
#################################################################