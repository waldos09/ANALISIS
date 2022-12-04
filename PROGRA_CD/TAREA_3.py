# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 15:02:26 2022

@author: waldo
"""

import pandas as pd #pandas para manipular datasets
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('C:/Users/waldo/Documents/Programas/PROGRA_CD/dataset/stats/League of Legends Champion Stats 12.1.csv', sep=';')

#print(dataset.head())

role = dataset['Role']
win = dataset['Win %']
#print(role)
#print(win)


w=1
b=0
# puntos de la recta
x = np.linspace(0,dataset['Pick %'].str.replace('[#,%,&]', '').astype(float, errors='raise').max())
y = w*x+b

# grafica de la recta
dataset.plot.scatter(x='Pick %',y='Win %')
plt.plot(x, y, '-r')
#plt.ylim(0,dataset['Win %'].str.replace('[#,%,&]', '').astype(float, errors='raise').max()*.5)
plt.show()


x = np.array(x)
y = np.array(y)
sx=sy=sxy=sx2=0
N = dataset['Pick %'].str.replace('[#,%,&]', '').count()
for i in range(0,N):
# Varianza
  sx=sum(x)
  sy=sum(y)
  sx2= sx*sx
  sy2= sy*sy#r
  sxy= sx*sy#r
a0 = (sx2*sy-sx*sxy)/(N*sx2-pow(sx,2)) #rango(offset)
a1 = (N*sxy-sx*sy)/(N*sx2-pow(sx,2)) #Pendiente de la media

# Covarianza de sxy
covsxy=sum(x*y)/N

#desviacion tipica
sx2R= np.sqrt(sx2)
sy2R= np.sqrt(sy2) 

#Coeficiente de coerrelacion
r = (covsxy/(sx2R*sy2R))
print('###############')
print('offset: ',a0)
print('Pendiente: ',a1)
print("covarianza sxy:",covsxy)
print("Coeficiente de Coerrelacion:", r)
print('###############')
