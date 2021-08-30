# -*- coding: utf-8 -*-
"""
Created on Fri May 14 11:49:40 2021

@author: PARTH
"""

import tkinter as tk
from tkinter import *
import os
import tkinter.font as tkFont
root = Toplevel() 
root.title("Image Inpainting")  # Adding a title
root.geometry('350x200')
#root.configure(background='grey')
bg = PhotoImage(file = "bgfinal.png")
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)
fontStyle = tkFont.Font(family="Lucida Grande", size=15,weight="bold")
fontStyle1 = tkFont.Font(family="Lucida Grande", size=30,weight="bold")

options = tk.StringVar(root)
options.set("Dataset Selection") # default value

l1 = tk.Label(root,  text='Select AnyOne',width=10,fg="#007bff" )  
l1.grid(row=2,column=2) 

om1 =tk.OptionMenu(root, options, "CelebA-HQ_512","CelebA-HQ_256", "places2-512x680")
om1.grid(row=4,column=1)


 

b1 = tk.Button(root,  text='RUN', command=lambda: my_show() )  
b1.grid(row=4,column=2) 

str_out=tk.StringVar(root)
str_out.set("Output")

l2 = tk.Label(root,  textvariable=str_out, width=15 )  
l2.grid(row=4,column=4) 

def my_show():
    str_out.set(options.get())
    code = "python painter_gmcnn.py --dataset "
    code+=options.get()
    if(options.get() == "CelebA-HQ_512"):
        code+=" --data_file ./imgs/celebahq_512x512/ --load_model_dir ./checkpoints/celebahq_512x512_freeform --random_mask 0 --img_shapes 512,512,3"
    elif(options.get() == "CelebA-HQ_256"):
        code+=" --data_file ./imgs/celebahq_256x256/ --load_model_dir ./checkpoints/celebahq_256x256_rect --random_mask 0"
    elif(options.get() == "places2-512x680"):
        code+= " --data_file ./imgs/places2-512x680/ --load_model_dir ./checkpoints/places2_512x680_freeform --random_mask 0 --img_shapes 512,680,3"
    
    #print(code)
    os.system(code)
    root.destroy()
root.mainloop()
