import numpy as np
import cv2
import matplotlib.pyplot as plt

from PIL import ImageTk, Image 
from tkinter import *
from tkinter import filedialog 
import random
from PIL import Image
import gc
import os
import glob
import socket
import tensorflow as tf
from inpaint_model import *
import argparse

import torch
from torchvision.models.segmentation import deeplabv3_resnet101
from torchvision import transforms

catval = 15
def make_deeplab(device):
    deeplab = deeplabv3_resnet101(pretrained=True).to(device)
    deeplab.eval()
    return deeplab

device = torch.device("cpu")
deeplab = make_deeplab(device)

def infer(batch_data,mask,reuse=False):
        shape=batch_data.get_shape().as_list()
        batch_gt=batch_data/127.5-1. 
        batch_incomplete=batch_gt*mask        
        image_p1, image_p2=RW_generator(batch_incomplete,mask,reuse=reuse)
        image_c2=batch_incomplete*mask+ image_p2*(1.-mask)
        image_c2=(image_c2+1.)*127.5
        return image_c2
    
deeplab_preprocess = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
 
def apply_deeplab(deeplab, img, device):
    input_tensor = deeplab_preprocess(img)
    input_batch = input_tensor.unsqueeze(0)
    with torch.no_grad():
        output = deeplab(input_batch.to(device))['out'][0]
    output_predictions = output.argmax(0).cpu().numpy()
    return (output_predictions == catval)

def gen_mask(f_name):
    img_orig = cv2.imread(f_name, 1)
    plt.imsave('./results/1.org.png',img_orig[:, :, ::-1])

    k = min(1.0, 1024/max(img_orig.shape[0], img_orig.shape[1]))
    img = cv2.resize(img_orig, None, fx=k, fy=k, interpolation=cv2.INTER_LANCZOS4)




    mask = apply_deeplab(deeplab, img, device)
    plt.imsave('./results/2.seg.png',mask)



    im_gray = cv2.imread('./results/2.seg.png', cv2.IMREAD_GRAYSCALE)
    (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    cv2.imwrite('./results/3.mask.png',im_bw)




def openfilename(): 

	filename = filedialog.askopenfilename(title ='select') 
	return filename 



height=216
width=216


model_path="./models"
file_out="./results"
        



def open_img():
        tf.reset_default_graph()
        file_test=openfilename()
        gen_mask(file_test)
        file_mask='./results/3.mask.png'

        
        mask1= cv2.imread(file_mask)
        
        img = Image.open(file_test) 

        img = img.resize((256, 256), Image.ANTIALIAS) 
        
        im1 = img
    
        img = ImageTk.PhotoImage(img) 

        # create a label 
        panel = Label(root, image = img) 

        panel.image = img 
        panel.grid(row = 2) 
        
        
        
        images=tf.placeholder(tf.float32,[1,height,width,3],name = 'image')
        mask=tf.placeholder(tf.float32,[1,height,width,1],name='mask')
        sess = tf.Session()        
        inpainting_result=infer(images,mask)
        saver_pre=tf.train.Saver()
        init_op = tf.group(tf.initialize_all_variables(),tf.initialize_local_variables()) 
        sess.run(init_op)
        saver_pre.restore(sess,tf.train.latest_checkpoint(model_path))
        
        
        test_mask = cv2.resize(mask1,(height,width))
        test_mask = test_mask[:,:,0:1]

        test_mask = 0. + test_mask//255
        test_mask[test_mask >= 0.5] = 1
        test_mask[test_mask <  0.5] = 0
        test_mask  = 1 -test_mask
        test_image = cv2.imread(file_test)[...,::-1]
        test_image = cv2.resize(test_image, (height,width))
        
        test_mask = np.expand_dims(test_mask,0)
        test_image = np.expand_dims(test_image,0)
        img_out=sess.run(inpainting_result,feed_dict={mask:test_mask,images:test_image})
        
        cv2.imwrite(file_out+"/5.big.png", img_out[0][...,::-1])
        cv2.imwrite(file_out+"/4.masked.png", test_image[0][...,::-1] * test_mask[0] + 255 * (1 - test_mask[0]))
        
        im =  cv2.imread("./results/1.org.png", cv2.IMREAD_COLOR)-cv2.imread(file_out+"/4.masked.png",cv2.IMREAD_COLOR)
        cv2.imwrite(file_out+"/6.output.png", im)
        
def open_img2(): 
    
    x =file_out+"/6.output.png"
    
    img = Image.open(x)
    
     
	
    img = img.resize((256, 256), Image.ANTIALIAS) 

    img = ImageTk.PhotoImage(img) 

    panel = Label(root, image = img) 
	
    panel.image = img 
    panel.grid(row = 2,column= 10) 
    
    
def show():
    global catval
    cat = {
        "Person":15,
        "Horse":13,
        "Car":7,
        "Bird":3
        
        }
    catval = cat[clicked.get()]





root = Tk() 
root.title("Demo")

#root.configure(background = "#FFFDD0")
bg = PhotoImage(file = "bgfinal.png")
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)
options = [
    "Person",
    "Horse",
    "Car",
    "Bird"
]
# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set( "Person" )
  
# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.config(bg="#39faf4")
drop.place(x=550, y=125)

root.geometry("660x300") 

root.configure(background='grey')


root.resizable(width = True, height = True) 

btn = Button(root, text ='open image',width=12, height=3, command = open_img ,bg="#39faf4").place(x=550, y=0) 
btn2 = Button(root, text ='execute',width=12, height=3, command = open_img2 ,bg="#39faf4").place(x=550, y=55) 
btn3 = Button( root , text = "set value" , command = show,width=12, height=1 ,bg="#39faf4").place(x=550, y=155)



root.mainloop() 

