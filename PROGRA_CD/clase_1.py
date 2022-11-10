# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from numpy import *
#from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

#crea figura y estructura de subplots(subfiguras)
fig, ax = plt.subplots(1,3,figsize=(12,4))
f=2

c=2

A=random.randint(-5,6,size=(f,c))
B=random.randint(-5,6,size=(f,c))

#indica el subplot a utlilizar
ax1=ax[0]

#pcolor para graficar arreglos bidimencionales
c= ax1.pcolor(A, cmap='Greys')
ax1.set_title('A')
plt.show()


AB=dot(A,B)
ax3 = ax[0]
plt.show()
