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

def insercion(A):
    for i in range(len(A)):
        for j in range(i,0,-1):
            if(A[j-1] > A[j]):
                aux=A[j]
                A[j]=A[j-1]
                A[j-1]=aux

print(file)
print("\n")

print("Iniciando ordenamiento")

insercion(file[:])


final=time.time()
finish=time.process_time()

print("\n\aFin del Ordenamiento")
print("\nTiempo de ejecucion del programa: "+str(final-inicio))
print("\nTiempo de ejecucion del CPU: "+str(finish-start))
print("\n")
print(file)