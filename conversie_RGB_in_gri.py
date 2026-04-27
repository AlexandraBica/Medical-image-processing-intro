# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 17:45:40 2026

"""

# conversie RGB in niveluri de gri
# pentru imaginile jpg si png

import os
import numpy as np
import matplotlib.pyplot as plt

img=[r'C:\Users\alexb\Desktop\Piese_PCLP\Medical-image-processing-intro\scintigrafia.jpg',r'C:\Users\alexb\Desktop\Piese_PCLP\Medical-image-processing-intro\test.png']
  
def rgb2gri(img_in, format):
    img_in=img_in.astype('float')
    s=img_in.shape
    if len(s)==3 and s[2]==3:
        if format=='png':
            img_out=(0.299*img_in[:,:,0]+0.587*img_in[:,:,1]+0.114*img_in[:,:,2])*255
        elif format=='jpg':
            img_out=0.299*img_in[:,:,0]+0.587*img_in[:,:,1]+0.114*img_in[:,:,2]
        img_out=np.clip(img_out, 0,255)
        img_out=img_out.astype('uint8')
        return img_out
    else:
        print('Conversia nu a putut fi realizata deoarece imaginea de intrare nu este, → color!')
        return img_in

for cale in img:
    img=plt.imread(cale)
    extensie = os.path.splitext(cale)[1][1:] # si pentru jpg si pentru png
    img_gri=rgb2gri(img, extensie)

    plt.figure()
     
    plt.subplot(1,2,1)
    plt.imshow(img)
    plt.title("Original")
   
    plt.subplot(1,2,2)
    plt.imshow(img_gri, cmap='gray')     
    plt.title("Nivel de gri")
     
    plt.show()
