# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 17:45:40 2026

"""

# afisarea planului de culoare
# pentru imaginile jpg si png
import os
import numpy as np
import matplotlib.pyplot as plt

imagini=[r'C:\Users\alexb\Desktop\Piese_PCLP\Medical-image-processing-intro\scintigrafia.jpg',r'C:\Users\alexb\Desktop\Piese_PCLP\Medical-image-processing-intro\test.png']
  

for i, cale in enumerate(imagini):
    img = plt.imread(cale)
    R = img[:,:,0]
    G=img[:,:,1]
    B=img[:,:,2]

    plt.subplot(1, len(imagini), i+1)
    plt.imshow(R, cmap='gray')

plt.show()



