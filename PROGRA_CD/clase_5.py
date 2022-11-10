# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 16:24:51 2022

@author: waldo
"""

f = open("/content/text.txt","r")
print(type(f))

for i in f:
  print(type(i))
  print(i)
  #split separa una cada de caracteres y los guarda en una lista
  #criterio de separacion el espacio y en csv la coma
  palabras = i.split()
  print(type(palabras))
  #mientras  no exita un reglon vacio va imprimir (imprime un parrafo)
  if(len(palabras)):
    print(palabras[0])

txt = ("          refresco         ")
print("A los alumnos les gusta el", txt)

x = txt.strip()
#strip quita espacios en blanco
print("A los alumnos les gusta el", x)

y = x.upper()
#pasa el texto a mayusculas
#lower() a minusculas
print(y)

z= y.lower()
print(z)