from tkinter import *

import os
##from PIL import Image, ImageTk
import tkinter.font as tkFont
root= Toplevel()
root.title('Image Inpainting')
root.geometry('1280x720')
#root.configure(background='grey')
bg = PhotoImage(file = "bgfinal.png")
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)
fontStyle = tkFont.Font(family="Lucida Grande", size=15,weight="bold")
fontStyle1 = tkFont.Font(family="Lucida Grande", size=30,weight="bold")
myLabel1 = Label(root,text="Main Menu",font=fontStyle1,fg="#007bff")
myLabel2 = Label(root,text="Home Page 2")
myLabel1.place(x=525,y=20)


# import example as e
# import runpy
# #runpy.run_module('runpyexample', run_name='__main__')
# import temp2
# import test2 
# import painter_gmcnn
# import subprocess




def b1():
    #myLabel3 = Label(root,text="Button Clicked")
    #myLabel3.pack()
    #os.system('python temp2.py')
    # e.ex()
    #runpy.run_module('temp2', run_name='__main__')
    os.system('python InpaintingMenu.py')
    root.destroy()
    #test2.Main()
    #painter_gmcnn.Main()
    # subprocess.run(['python',"temp2.py"],capture_output=True)
    # cmd = 'python temp2.py'.split()
    # proc = subprocess.run(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    # print(proc.stdout)

myButton1 = Button(root,text="Image Inpainting",command = b1,padx=20,width=15,height=8,font=fontStyle, fg="#007bff",bg="#39faf4")
#myButton1.pack()
myButton1.place(x=25, y=350)
myButton2 = Button(root,text="Background Remover",command = b1,padx=20,width=15,height=8,font=fontStyle, fg="#007bff",bg="#39faf4")
myButton2.place(x=525,y=350)
myButton3 = Button(root,text="Object Remover",command = b1,padx=20,width=15,height=8,font=fontStyle, fg="#007bff",bg="#39faf4")
myButton3.place(x=1025,y=350)
root.mainloop()
