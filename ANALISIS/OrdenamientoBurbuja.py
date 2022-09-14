#Abarca Garcia Diego Uriel
#Acevedo García Irving
#Carmona Bartolome Aldo Armando
#Estrada Chavarria Alexis
#13-sep-2022
#Grupo. 3AM1
import numpy as np
import time

start=time.process_time()
inicio=time.time()

file = np.loadtxt("numeros10millones.txt",dtype="int")

def bubbleSort(nums):
    intercambio=True
    while(intercambio):
        intercambio = False

        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
                intercambio=True

print(file)
print("\n")

print("Iniciando ordenamiento")

bubbleSort(file[:])

final=time.time()
finish=time.process_time()

print("\n\aFin del Ordenamiento")
print("\nTiempo de ejecucion del programa: "+str(final-inicio))
print("\nTiempo de ejecucion del CPU: "+str(finish-start))
print("\n")
print(file)
