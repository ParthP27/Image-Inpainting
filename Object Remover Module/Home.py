from tkinter import *

import os
##from PIL import Image, ImageTk
import tkinter.font as tkFont
root= Toplevel()
root.title('Image Inpainting')
root.geometry('1280x720')
#root.configure(background='grey')
bg = PhotoImage(file = "my.png")
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)
fontStyle = tkFont.Font(family="Lucida Grande", size=15,weight="bold")
fontStyle1 = tkFont.Font(family="Lucida Grande", size=30,weight="bold")
myLabel1 = Label(root,text="Main Menu",font=fontStyle1,fg="#007bff")
myLabel2 = Label(root,text="Home Page 2")
myLabel1.place(x=525,y=20)




def b1():
    os.system("python GUI.py")
    

myButton1 = Button(root,text="Image Inpainting",command = b1,padx=20,width=15,height=8,font=fontStyle, fg="#007bff",bg="#39faf4")
#myButton1.pack()
myButton1.place(x=25, y=350)
myButton2 = Button(root,text="Background Remover",command = b1,padx=20,width=15,height=8,font=fontStyle, fg="#007bff",bg="#39faf4")
myButton2.place(x=525,y=350)
myButton3 = Button(root,text="Object Remover",command = b1,padx=20,width=15,height=8,font=fontStyle, fg="#007bff",bg="#39faf4")
myButton3.place(x=1025,y=350)
root.mainloop()
