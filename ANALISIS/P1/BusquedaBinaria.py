"""
Programa: Busqueda Binaria
Función: Buscar un elemento (empleando la busqueda binaria) dentro de un arreglo, el cual ha recivido previamente 10 millones de numeros a partir de la extracción de dichos elementos de un archivos, que posteriormente seran ordenados de manera ascendente (utilizando el ordenamiento shell) para comenzar con la busqueda
Fecha: 16/10/22
Version: 1.0
Autor: Estrada Chavarría Alexis
"""
import numpy as np
import time

#Tiempo de inicio para el programa
inicio=time.time()
start=time.process_time()

print("Extrayendo archivo")

file=np.loadtxt("numeros10millones.txt",dtype="int")

print("\nExtraccion Terminada")

#Se debe ordenar la matriz para utilizar la busqueda binaria

def shell_sort(l):
    gap = len(l) // 2
    while gap > 0:
        for i in range(gap, len(l)):
            temp = l[i]
            j = i
            while j>=gap and l[j-gap] > temp:
                l[j] = l[j-gap]
                j = j-gap
            l[j] = temp
        gap = gap//2
    return l


def busqueda_bin(arr, elemento):
    
    print ("\nIniciando Busqueda")

    izq=0

    der=len(arr)-1

    while(izq<=der):
        mitad=(izq+der)//2

        if(arr[mitad]==elemento):
            print("\nBusqueda Terminada")
            return True
        elif (arr[mitad]<elemento):
            izq=mitad+1
        else:
            der=mitad-1
    
    print("\nBusqueda Terminada")
    return False

def tiempos(resultado,elemento,inicio,start,fin,finish,inicio_ord,start_ord,fin_ord,finish_ord):
    
    if(resultado):
        print("Se encontro el elemento " + str(elemento))
    else:
        print("No encontro el elemento " + str(elemento))

    
    print("\n\t********************Tiempos del ordenamiento********************")
    print("\nEjecución del programa = " + str(fin_ord-inicio_ord))
    print("\nEjecución del CPU = " + str(finish_ord-start_ord))

    print("\n\t********************Tiempos de la busqueda********************")
    print("\nEjecución del programa = " + str((fin-inicio)-(fin_ord-inicio_ord)))
    print("\nEjecución del CPU = " + str((finish-start)-(finish_ord-start_ord)))

    print("\n\t********************Tiempos Totales(Busqueda-Ordenamiento)********************")
    print("\nEjecución del programa = " + str(fin-inicio))
    print("\nEjecución del CPU = " + str(finish-start))


print(file)
print("\n")

#Tiempo de inicio para el ordenamiento
inicio_ord=time.time()
start_ord=time.process_time()

print("Iniciando ordenamiento")

shell_sort(file)

print("\n\aFin del Ordenamiento")
print(file)

#Fin del timepo del ordenamiento
fin_ord=time.time()
finish_ord=time.process_time()

elemento = 2147483603


#Fin del tiempo del programa
fin=time.time()
finish=time.process_time()

resultado=busqueda_bin(file,elemento)

if(resultado):
    tiempos(resultado,elemento,inicio,start,fin,finish,inicio_ord,start_ord,fin_ord,finish_ord)
else:
    tiempos(resultado,elemento,inicio,start,fin,finish,inicio_ord,start_ord,fin_ord,finish_ord)
