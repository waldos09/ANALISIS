# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 16:21:06 2022

@author: waldo
"""

### TAREA DE MATRICES ###
### Carmona Bartolome Aldo Armando 3AM1 ###

from numpy import *
import matplotlib.pyplot as plt
#crea figura y estructura de subplots(subfiguras)
fig, ax = plt.subplots(1,3,figsize=(12,4))
#filas y columnas
f=3
c=3
#matrices
A=random.randint(-5,6,size=(f,c))
B=random.randint(-5,6,size=(f,c))

#indica el subplot a utlilizar
ax1=ax[0]
ax2=ax[1]
ax3=ax[2]

#imprmimos las matrices
print(A,'\n')
print(B,'\n')

#swap
A[[0,2]] = A[[2,0]]
B[[0,2]] = B[[2,0]]
print(A,'\n')
print(B,'\n')

#pcolor para graficar arreglos bidimencionales
c= ax1.pcolor(A, cmap='Greys')
ax1.set_title('A')
d = ax2.pcolor(B, cmap='Greys')
ax2.set_title('B')
#A*B
AB=dot(A,B)
ab = ax3.pcolor(AB, cmap='Greys')
ax3.set_title('AB')

#imprime ab
AB[[0,2]] = AB[[2,0]]
print(AB)

plt.show()