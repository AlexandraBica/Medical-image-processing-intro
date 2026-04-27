# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 19:19:55 2026

"""

# histograma, citire, afisare
import os
import numpy as np
import matplotlib.pyplot as plt

# citirea imaginii
cale=r'C:\Users\alexb\Desktop\Piese_PCLP\Medical-image-processing-intro'
cale_img=os.path.join(cale,'scintigrafia.jpg')
img=plt.imread(cale_img)

# histograma
h,_=np.histogram(img, bins=256, range=[0,256])

plt.figure('Histograma imag scintigrafia.jpg')
plt.bar(range(256),h)
plt.show()

# afisarea imaginii
plt.figure('scintigrafia')
plt.imshow(img)
plt.show()

plt.figure('scintigrafia2')
plt.imshow(img,cmap='gray', vmin=0, vmax=255)
plt.show()

