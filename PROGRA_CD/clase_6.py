# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 16:26:07 2022

@author: waldo
"""

import math
import matplotlib.pyplot as plt
import numpy as np
import string 
import csv

x = np.linspace(0,10,50)
## crea un arreglo de tam 50 que inicia en 0 termina en 10
dy = 0.8

y= np.sin(x) + dy + np.random.randn(50)
yy=np.random.randn(50000)

#histograma
plt.hist(yy,bins=100)
print(np.mean(yy))
#desviacion estandar
print(np.std(yy))

print(yy)


fig,ax = plt.subplots(1,1, figsize=(4,4))

nombre='C:/Users/waldo/Documents/PROGRA_CD\DB/csv_camaras_1.csv'
with open(nombre) as csvfile:
  lector=csv.reader(csvfile,delimiter=',')#devuelve un objeto lector que sera iterado sobre las lienas del archivo
  for fila in lector: #itera el objeto lector
    x=(','.join (fila)) #crea una cadena con los elementos de ada registro del archivo csv
    registro=x.split(',')
    #print(registro)
    ax.scatter(registro[2],registro[3])
    #plt.show()
#plt.errorbar(x,y,yerr=dy, fmt='.k',capsize = 5)
plt.show()