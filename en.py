#######################################################
from encrypt import encryptor
from tkinter import *
import os
from tkinter.filedialog import askopenfilename
encr = Tk()
encr.geometry("510x300")
encr.title("Image Encryption")
encr.resizable(False,False)
#Function Defs
##############################################################
def browsefunc():
    global filename
    filename=askopenfilename(filetypes=(("PNG Files", "*.png;*.PNG"),("JPEG files", "*.jpg;*.JPG") ))
    e.config(text=filename)
    e.delete(0,END)
    e.insert(0,filename)

def go_home():
	encr.destroy()
	import main

def start_encrypting():
    global x
    x = e.get()
    encryptor(x)
#input Box    
###############################################################
e=Entry(encr,width=70,borderwidth=1)

#Button defs
###############################################################
l = Label(encr, text = "Location Of File To Encrypt")
button_browse = Button(encr, text="Browse", command=browsefunc)
button_back = Button(encr,text = "Go Back To Home",padx=40,pady=20,command=go_home)
button_encrypt = Button(encr,text = "Start Encrypting",padx=40,pady=20,command=start_encrypting ) 


#Button View format
#################################################################
l.place(x=10,y=30)
button_browse.place(x=450,y=55)
#button_decrypy.place(x=310,y=30)
button_back.place(x=35,y=185)
button_encrypt.place(x=300,y=185)
e.place(x=15,y=60)

#run
##################################################################
encr.mainloop()
#################################################################