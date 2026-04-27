# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 21:45:45 2026

@author: alexb
"""

# afisarea planului de culoare
# pentru imaginile jpg si png
import os
import numpy as np
import matplotlib.pyplot as plt

cale=r'C:\Users\alexb\Desktop\Piese_PCLP\Medical-image-processing-intro'
cale_img=os.path.join(cale,'scintigrafia.jpg')

img=plt.imread(cale_img)
R = img[:,:,0]

# Histograma ca nr de aparitii
h,_ = np.histogram(R, bins=256, range=(0,256))

plt.figure()
plt.bar(range(256),h)
plt.title("Histograma ca nr de aparitii")
plt.xlabel("Nivel de gri")
plt.ylabel("Nr de aparitii")
plt.show()

# Histograma ca densitate de probabilitate
h_prob = h / h.sum() #impart la nr total de pixeli

plt.figure()
plt.bar(range(256),h_prob)
plt.title("Histograma ca densitate de probabilitate")
plt.xlabel("Nivel de gri")
plt.ylabel("Probabilitate de aparitie")
plt.show()

# Histograma cumulativa ca nr de aparitii
h_cumulat=np.cumsum(h)

plt.figure()
plt.plot(range(256),h_cumulat)
plt.title("Histograma cumulativa")
plt.xlabel("Nivel de gri")
plt.ylabel("Nr de aparitii")
plt.show()

# Histograma cumulativa ca probabilitate
h_cumulat2=np.cumsum(h_prob)

plt.figure()
plt.plot(range(256),h_cumulat2)
plt.title("Histograma cumulativa")
plt.xlabel("Nivel de gri")
plt.ylabel("Probabilitate de aparitie")
plt.show()
