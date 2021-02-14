import inspect
import json

def print_this(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return str([k for k,v in callers_local_vars if v is var][0])

import random
import cv2
import numpy as np
thelist = [1,2,3,4,5,6,7,8]
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
anslist = []
x = 0
text = input().split()
dict1 = {

}
for i in text:
    x = random.choice(thelist)
    thelist.remove(x)
    dict1[f"img{x}"] = i

# hor = np.stack(img1, img2)

# for j in dict1.keys()[2:]:
#     hor = np.stack(hor,j)

with open("dict.json", "w") as outfile:
    json.dump(dict1, outfile)

for m in list(dict1.keys()):
    for n in yolist:
        if (print_this(n)) == m:
            anslist.append(n)
            break

hor = np.concatenate(anslist,1)

cv2.imshow("horizontal", hor)

print(cv2.imwrite(r"C:\Users\Apoorv Kant\Desktop\Image Encrypter\final.png", hor))

cv2.waitKey(0)

# print(anslist)

