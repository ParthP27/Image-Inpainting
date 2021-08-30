# -*- coding: utf-8 -*-
"""
Created on Sat May 15 20:23:23 2021

@author: sonib
"""
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 18:38:05 2021

@author: sonib
"""

# import math
# from PIL import Image, ImageDraw
  
# w, h = 220, 190
# shape = [(40, 40), (w - 10, h - 10)]
  
# # creating new Image object
# img = Image.new("RGB", (w, h))
  
# # create line image
# img1 = ImageDraw.Draw(img)  
# img1.line(shape, fill =(128,128,128), width =15 )
# img.show()
# print((0,0)+(256,256))


# from PIL import Image, ImageDraw

# with Image.open(r"F:\college\sem 8\Project CP442\mywork\GUI\004.png") as im:

#     draw = ImageDraw.Draw(im)
#     draw.line((0, 0) + im.size, fill=128)
#     draw.line((0, im.size[1], im.size[0], 0), fill=128)

#     # write to stdout
#     im.save("F:\college\sem 8\Project CP442\mywork\GUI\my.PNG")

# This show image properly 
# from tkinter import *
# from PIL import Image, ImageTk
# root = Tk()
# root.geometry('256x256')
# canvas = Canvas(root,width=256,height=256)
# canvas.pack()
# load.pilImage = Image.open("my.png")
# #load.pilImage.thumbnail((256,256))
# image = ImageTk.PhotoImage(load.pilImage)
# imagesprite = canvas.create_image(0,0,image=image,anchor=NW)
# root.mainloop()


from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from tkinter.filedialog import asksaveasfilename as saveAs
import tkinter.filedialog as tkFileDialog
import os

def load():
        filename = tkFileDialog.askopenfilename(initialdir='.',
                                                     title="Select file",
                                                     filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"),
                                                                ("all files", "*.*")))
        load.filename_ = filename.split('/')[-1][:-4]
        filepath = '/'.join(filename.split('/')[:-1])
        #print(filename,filename_, filepath)
        
        load.pilImage = Image.open(filename)
        load.image = ImageTk.PhotoImage(load.pilImage)
        load.imagesprite = canvas.create_image(0,0,image=load.image,anchor=NW)
        load.draw = ImageDraw.Draw(load.pilImage)



def save():
    load.pilImage.save("F:\college\sem 8\Project CP442\mywork\Project\examples\places2\images\{0}.png".format(load.filename_))
    image2.save("F:\college\sem 8\Project CP442\mywork\Project\examples\places2\masks\{0}.png".format(load.filename_))
    os.system("python test.py --checkpoints ./checkpoints/places2 --input ./examples/places2/images --mask ./examples/places2/masks --output ./checkpoints/results")
    
def activate_paint(e):
    global lastx, lasty
    canvas.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y

def paint(e):
    global lastx, lasty
    x, y = e.x, e.y
    canvas.create_line((lastx, lasty, x, y),fill="white", width=10)

    load.draw.line((lastx, lasty, x, y), fill='white', width=10)
    draw2.line((lastx, lasty, x, y), fill='white', width=10)
    lastx, lasty = x, y
def clear():
    canvas.delete('all')
def exitt():
    exit()

win = Tk()
win.title("Paint - made in Python")
lastx, lasty = None, None

canvas = Canvas(win,width=256,height=256)
canvas.pack()
# load.pilImage = Image.open("my.jpg")
# draw = ImageDraw.Draw(load.pilImage)
# #load.pilImage.thumbnail((256,256))
# image = ImageTk.PhotoImage(load.pilImage)
# imagesprite = canvas.create_image(0,0,image=image,anchor=NW)

# this is for mask image 
image2 = Image.new('RGB', (256, 256), 'black')
draw2 = ImageDraw.Draw(image2)

canvas.bind('<1>', activate_paint)
canvas.pack(expand=YES, fill=BOTH)

save_ = Button(text="Save image", command=save)
save_.pack()

save_ = Button(text="Load image", command=load)
save_.pack()

reset=Button(text='Reset canvas',command=clear)
reset.pack(side=LEFT)

_exit=Button(text='Exit',command=exitt)
_exit.pack(side=RIGHT)
win.mainloop()









# cv = Canvas(win, width=640, height=480, bg='white')
# image1 = PIL.Image.new('RGB', (640, 480), 'white')











