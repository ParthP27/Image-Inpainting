from tkinter import *
import runpy

import os
##from PIL import Image, ImageTk
import tkinter.font as tkFont


def b1():
    os.system('python demo1.py')




root1= Toplevel()
root1.title('Image Inpainting')
root1.geometry('1280x720')
#root.configure(background='grey')
bg = PhotoImage(file = "bgfinal1.png")
label1 = Label( root1, image = bg)
label1.place(x = 0, y = 0)
fontStyle = tkFont.Font(family="Lucida Grande", size=15,weight="bold")
fontStyle1 = tkFont.Font(family="Lucida Grande", size=30,weight="bold")
myLabel1 = Label(root1,text="Main Menu",font=fontStyle1,fg="#007bff")
myLabel2 = Label(root1,text="Home Page 2")
myLabel1.place(x=525,y=20)

myButton1 = Button(root1,text="Image Inpainting",command = b1,padx=20,width=15,height=8,font=fontStyle, fg="#007bff",bg="#39faf4")
#myButton1.pack()
myButton1.place(x=25, y=350)
myButton2 = Button(root1,text="Background Remover",command = b1,padx=20,width=15,height=8,font=fontStyle, fg="#007bff",bg="#39faf4")
myButton2.place(x=525,y=350)
myButton3 = Button(root1,text="Object Remover",command = b1,padx=20,width=15,height=8,font=fontStyle, fg="#007bff",bg="#39faf4")
myButton3.place(x=1025,y=350)
root1.mainloop()

