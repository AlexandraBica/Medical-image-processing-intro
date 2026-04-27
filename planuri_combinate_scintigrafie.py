# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 15:55:01 2026

@author: alexb
"""
# planuri combinate pentru obtinerea imaginilor color

import os
import numpy as np
import matplotlib.pyplot as plt
cale=r'C:\Users\alexb\Desktop\Piese_PCLP\Medical-image-processing-intro'
img=plt.imread(os.path.join(cale ,'scintigrafia.jpg'))

R=img[:,:, 0] 
G=img[:,:, 1]
B=img[:,:, 2]
h,_= np.histogram(R, bins=256, range=(0,256)) 
h_prob=h/h.sum() 
h_cumulat=np.cumsum(h_prob)

img_new=np.zeros((img.shape[0], img.shape[1],3), dtype='uint8')
img_new[:,:,0]=G
img_new[:,:,1]=G
img_new[:,:,2]=G

plt.figure()
plt.imshow(img_new)
plt.show()