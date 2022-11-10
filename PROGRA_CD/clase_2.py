# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 16:21:42 2022

@author: waldo
"""

##### 17 OCT 2022 ###
### fUNCION : Intruccion que puede tomar entrdas y devueve una salida correspondiente ###
import numpy as np
import matplotlib.pyplot as plt
def myprint(mesage='HOla mundo'):
  print(mesage)

myprint()
myprint('buen dia')  

n = 5
def tabla(n):
  for i in range(11):
    print(n*i)

tabla(n)

def caminante():
  x=10
  lista=[]
  while(x>=0):
    lista.append(x)
    x+=np.random.random()-0.5
    if(x<3.5):
      break
  return lista

y =caminante()

plt.plot(y)
plt.show()