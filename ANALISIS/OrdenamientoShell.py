#Abarca Garcia Diego Uriel
#Acevedo Garcia Irving
#Carmona Bartolome Aldo Armando
#Estrada Chavarria Alexis
#13-sep-2022
#Grupo. 3AM1
import numpy as np
import time

start=time.process_time()
inicio=time.time()

file = np.loadtxt("numeros10millones.txt",dtype="int")

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

print(file)
print("\n")

print("Iniciando ordenamiento")

shell_sort(file[:])


final=time.time()
finish=time.process_time()

print("\n\aFin del Ordenamiento")
print("\nTiempo de ejecucion del programa: "+str(final-inicio))
print("\nTiempo de ejecucion del CPU: "+str(finish-start))
print("\n")
print(file)