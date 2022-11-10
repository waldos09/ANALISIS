# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 16:37:29 2022

@author: waldo
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import string
import csv


fig,ax = plt.subplots(4, figsize=(10,10))

#plot para maxima
ax1 = ax[0]
ax2 = ax[1] 
ax3 = ax[2]
ax4 = ax[3]


#maxima resolucion
maxr = []
#minima resolucion
minr = []

#año
year = []

data = 'C:/Users/waldo/Documents/PROGRA_CD\DB/csv_camaras_1_reducida.csv'
with open(data,'r') as csvfile:
    read = csv.reader(csvfile)
    next(read)
    for fila in read:        
        x=(','.join(fila))
        log = x.split(',')
        print(log)
        maxr.append(log[2])
        minr.append(log[3])
        year.append(log[1])
        ax3.scatter(year,maxr)
        ax3.scatter(year,minr)
        
#### HISTOGRAMAS DE RESOLUCIONJES ####
#plt.hist(maxr, bins=10)
maxrg = ax1.hist(maxr, bins=10)
ax1.set_title('Max Resolution')

#plt.hist(minr, bins=10)
minrg = ax2.hist(minr, bins=10)
ax2.set_title('Min resolution')
#print(minr)

####COMPARACION AÑO RESOLUCIONES ####
#compy = ax3.plot(year, maxr)
#ax4.set_title('Year vs Max resolution')
#compy = ax3.plot(year, minr)
#ax5.set_title('Year vs Min resolution')
#### MEDIA Y DESVICION ESTANDAR ####
maxrs = list(map(float, maxr))
minrs = list(map(float, minr))
print('MEDIA MAX:')
print(np.mean(maxrs))
print('MEDIA MIN:')
print(np.mean(minrs))
print('\n ############ \n')
print('DISTRIBUCION MAX')
print(np.std(maxrs))
print('DISTRIBUCION MIN')
print(np.std(minrs))

ax4.plot(maxr)
ax4.plot(minr)

print(maxr)
print(minr)

plt.show()

