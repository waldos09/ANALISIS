#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programa: Busqueda Secuencial
Función: Buscar un elemento (empleando la busqueda secuencial) dentro de un arreglo, el cual ha recivido previamente 10 millones de numeros a partir de la extracción de dichos elementos desordenados dentro de un archivo
Fecha: 16/10/22
Version: 1.0
Autor: Estrada Chavarría Alexis
"""

import numpy as np
import time

inicio=time.time()
start=time.process_time()

print("Extrayendo archivo")

file=np.loadtxt("numeros10millones.txt",dtype="int")

print("\nExtraccion Terminada")

def busqueda_sec(arr,elemento):
    print("\nIniciando Busqueda")
    for i in range(len(arr)):
        if(arr[i]==elemento):
            print("\nBusqueda Terminada\n")
            return True
    print("\nBusqueda Terminada\n")
    return False

elemento=2147483603

fin=time.time()
finish=time.process_time()

if(busqueda_sec(file,elemento)):
    print("Se encontro el elemento " + str(elemento))
    print("\nTiempo de ejecución del programa = " + str(fin-inicio))
    print("\nTimepo de ejecución del CPU = " + str(finish-start))
else:
    print("No encontro el elemento " + str(elemento))
    print("\nTiempo de ejecución del programa = " + str(fin-inicio))
    print("\nTimepo de ejecución del CPU = " + str(finish-start))