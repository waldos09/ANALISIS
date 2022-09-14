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

def cocktail_sort(vector):
    permutation,dirección,actual = True,1,0
    comienzo,fin = 0,len(vector)-2
    while permutation == True:
        permutation = False
        while (actual<fin and dirección==1) or \
        (actual>comienzo and dirección==-1) :
            # Prueba si intercambio
            if vector[actual] > vector[actual + 1]:
                permutation = True
                # Intercambiamos los dos elementos
                vector[actual], vector[actual + 1] = \
                vector[actual + 1],vector[actual]
            actual = actual + dirección
        # Cambiar la dirección de desplazamiento
        if dirección==1:
            fin = fin - 1
        else:
            comienzo = comienzo + 1
        dirección = -dirección
    return vector  

print(file)
print("\n")

print("Iniciando ordenamiento")

cocktail_sort(file[:])

final=time.time()
finish=time.process_time()

print("\n\aFin del Ordenamiento")
print("\nTiempo de ejecucion del programa: "+str(final-inicio))
print("\nTiempo de ejecucion del CPU: "+str(finish-start))
print("\n")
print(file)
