# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 16:24:16 2022

@author: waldo
"""

import matplotlib.pyplot as plt
import string 
import csv

fig,axes = plt.subplots(2,1, figsize=(4,4))
fila2=[]
fila3=[]
nombre='/content/drive/MyDrive/csv_camaras_1.csv'
with open(nombre) as csvfile:
  lector=csv.reader(csvfile,delimiter=',')#devuelve un objeto lector que sera iterado sobre las lienas del archivo
  for fila in lector: #itera el objeto lector
    x=(','.join (fila)) #crea una cadena con los elementos de ada registro del archivo csv
    registro=x.split(',')
    #print(registro)
    fila2.append(registro[2])
    fila3.append(registro[3])

ax=axes[0]
ax.scatter(fila2,fila3)
ax=axes[1]
ax.bar(fila2,fila3)
plt.show()

#####
data = open(nombre)
lines = data.readlines()
b=0
for line in lines:
  if(b>0):
    x0,x1,x2,x3,x4,x5=line.split()
    x = float(x2)
    y= float(x3)
    print(x,y)
  b+=1