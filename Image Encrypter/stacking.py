import numpy as np
import cv2

img1 = cv2.imread(r"C:\Users\Apoorv Kant\Desktop\Image Encrypter\i1.jpeg")
img2 = cv2.imread(r"C:\Users\Apoorv Kant\Desktop\Image Encrypter\i2.jpeg")
print(img1.shape) 
print(img2.shape)

dsize = (100, 100)

img1 = cv2.resize(img1, dsize)
img2 = cv2.resize(img2, dsize)

hor = np.hstack((img2, img1))
ver = np.vstack((img2, img1))

cv2.imshow("Vertical", ver)
cv2.imshow('Horizontal', hor)

cv2.waitKey(0)