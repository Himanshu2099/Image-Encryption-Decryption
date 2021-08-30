#######################################################
from tkinter import *
root = Tk()
root.geometry("600x300")
root.title("Visual Cryptography")
root.resizable(False,False)
#Function defs
##############################################################
def encrypt_page():
    root.destroy()
    import en

def decrypt_page():
    root.destroy()
    import de

#input Box    
###############################################################

#Button defs
###############################################################
button_encrypy = Button(root,text = "Click Here To\nEncrypt Image",padx=40,pady=20,command=encrypt_page)
button_decrypy = Button(root,text = "Click Here To\nDecrypt Image",padx=40,pady=20,command=decrypt_page)
button_exit = Button(root,text = "Click Here To\nExit",padx=40,pady=20,command=lambda: exit())


#Button View format
#################################################################
button_encrypy.place(x=110,y=30)
button_decrypy.place(x=310,y=30)
button_exit.place(x=210,y=175)


#run
##################################################################
root.mainloop()
#################################################################