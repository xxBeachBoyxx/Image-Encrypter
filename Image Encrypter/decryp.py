import cv2
import numpy as np
from PIL import Image
import inspect
import json


def print_this(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return str([k for k,v in callers_local_vars if v is var][0])

def is_similar(image1, image2):
    return image1.shape == image2.shape and not(np.bitwise_xor(image1,image2).any())

img1 = cv2.imread(r"C:\Users\Apoorv Kant\Desktop\Image Encrypter\i1.png")
img2 = cv2.imread(r"C:\Users\Apoorv Kant\Desktop\Image Encrypter\i2.png")
img3 = cv2.imread(r"C:\Users\Apoorv Kant\Desktop\Image Encrypter\i3.png")
img4 = cv2.imread(r"C:\Users\Apoorv Kant\Desktop\Image Encrypter\i4.png")
img5 = cv2.imread(r"C:\Users\Apoorv Kant\Desktop\Image Encrypter\i5.png")
img6 = cv2.imread(r"C:\Users\Apoorv Kant\Desktop\Image Encrypter\i6.png")
img7 = cv2.imread(r"C:\Users\Apoorv Kant\Desktop\Image Encrypter\i7.png")
img8 = cv2.imread(r"C:\Users\Apoorv Kant\Desktop\Image Encrypter\i8.png")

dsize = (50, 50)

img1 = cv2.resize(img1, dsize)
img2 = cv2.resize(img2, dsize)
img3 = cv2.resize(img3, dsize)
img4 = cv2.resize(img4, dsize)
img5 = cv2.resize(img5, dsize)
img6 = cv2.resize(img6, dsize)
img7 = cv2.resize(img7, dsize)
img8 = cv2.resize(img8, dsize)

yolist = [img1,img2,img3,img4,img5,img6,img7,img8]

x = 0
y = 0
h = 50
w = 50
keydict = {}
with open("dict.json", mode='r') as infile:
    keydict = json.load(infile)


while ((x < 400) and (y < 400)):
    img = cv2.imread("final.png")
    crop_img = img[x:x+h, y:y+w]
    for re in yolist:
        if (is_similar(crop_img,re)):
            qui = print_this(re)
            print(keydict[f"{qui}"], end=" ")
            
    y += h
    



    



