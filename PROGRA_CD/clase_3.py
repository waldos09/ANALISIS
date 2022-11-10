# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 16:24:08 2022

@author: waldo
"""

import matplotlib.pyplot as plt
import string 
import csv

fig,ax = plt.subplots(1,1, figsize=(4,4))

nombre='/content/drive/MyDrive/csv_camaras_1.csv'
with open(nombre) as csvfile:
  lector=csv.reader(csvfile,delimiter=',')#devuelve un objeto lector que sera iterado sobre las lienas del archivo
  for fila in lector: #itera el objeto lector
    x=(','.join (fila)) #crea una cadena con los elementos de ada registro del archivo csv
    registro=x.split(',')
    #print(registro)
    ax.scatter(registro[2],registro[3])
    #plt.show()