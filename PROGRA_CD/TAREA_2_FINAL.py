# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 17:28:47 2022

@author: waldo
"""

#### TAREA 2 MEJOR ####

import pandas as pd #pandas para manipular datasets
import numpy as np
import matplotlib.pyplot as plt
"""
def dejar_solo_cifras(txt):
  return "".join(c for c in txt if c.isdigit())
"""
dataset = pd.read_csv('C:/Users/waldo/Documents/Programas/PROGRA_CD/dataset/stats/League of Legends Champion Stats 12.1.csv', sep=';')

#print(dataset.head())

"""
El DATASET ESTA FORMADO CONTIENE
 Name || Class || Role || Score || Trend || Win % || Role % || Pick % || Ban % || KDA
"""
champ = dataset['Name'] ######
clase = dataset['Class'] #####
rolerate = dataset['Role'] ####
win = dataset['Win %'] #####
ban = dataset['Ban %'] #####
rolepick = dataset['Role %']
pick = dataset['Pick %'] 

#win = win.map(dejar_solo_cifras)
win = win.str.replace('[#,%,&]', '') # quitar  # % y $ de los datos del winrate
win = win.astype(float, errors='raise') #cambiar a flotantes
#print(type(win))
#print(win)


ban = ban.str.replace('[#,%,&]', '') # quitar  # % y $ de los datos del winrate
ban = ban.astype(float, errors='raise') #cambiar a flotantes
#print(type(ban))


#Roles = Top, Mid, ADC, Support or Jungle

clases = dataset.groupby(['Class']).size().reset_index(name='No de champs')
#grupby cuenta la cant de datos q hay y size cuantas veces se repite cada uno
#reset_index agrega una columna a clases con el la cantidad de repeticiones q tiene cada clase

#print(clases)  #imprime los tipos de clases y la cantidad de champs q hay en cada una
# marksman es tirador xD
roles = dataset.groupby(['Role']).size().reset_index(name='No de champs')
#print(roles)


rolxclase = dataset.groupby(['Role' , 'Class']).size().reset_index(name='No de champs') #lo mismo pero ahora tienes rol clase y sus cant
"""
otra forma es dataset[(dataset['Role'] == 'MID')].groupby(['Class']).size().reset_index(name='No de champs')
"""
#separas por cada rol q hay
adc = rolxclase[(rolxclase['Role'] == 'ADC')]
sup = rolxclase[(rolxclase['Role'] == 'SUPPORT')]
mid= rolxclase[(rolxclase['Role'] == 'MID')]
top = rolxclase[(rolxclase['Role'] == 'TOP')]
jg= rolxclase[(rolxclase['Role'] == 'JUNGLE')]

#print(jg)
#print(rolxclase)
#print(rolxclase[(rolxclase['Role'] == 'ADC')]) # solo imprime los del rol de ADC
#print(list(adc['Class']))

#MID WINRATE
rolxwinMID = dataset[(dataset['Role'] == 'MID')]
rolxwinMID = rolxwinMID['Win %'].str.replace('[#,%,&]', '') # quitar  # % y $ de los datos del winrate
rolxwinMID = rolxwinMID.astype(float, errors='raise') #cambiar a flotantes
#print(rolxwinMID)
#TOP WINRATE
rolxwinTOP = dataset[(dataset['Role'] == 'TOP')]
rolxwinTOP = rolxwinTOP['Win %'].str.replace('[#,%,&]', '') # quitar  # % y $ de los datos del winrate
rolxwinTOP = rolxwinTOP.astype(float, errors='raise') #cambiar a flotantes
#print(rolxwinTOP)
#ADC WINRATE
rolxwinADC = dataset[(dataset['Role'] == 'ADC')]
rolxwinADC = rolxwinADC['Win %'].str.replace('[#,%,&]', '') # quitar  # % y $ de los datos del winrate
rolxwinADC = rolxwinADC.astype(float, errors='raise') #cambiar a flotantes
#print(rolxwinMID)
#SUP WINRATE
rolxwinSUP = dataset[(dataset['Role'] == 'SUPPORT')]
rolxwinSUP = rolxwinSUP['Win %'].str.replace('[#,%,&]', '') # quitar  # % y $ de los datos del winrate
rolxwinSUP = rolxwinSUP.astype(float, errors='raise') #cambiar a flotantes
#print(rolxwinMID)
#JG WINRATE
rolxwinJG = dataset[(dataset['Role'] == 'JUNGLE')]
rolxwinJG = rolxwinJG['Win %'].str.replace('[#,%,&]', '') # quitar  # % y $ de los datos del winrate
rolxwinJG = rolxwinJG.astype(float, errors='raise') #cambiar a flotantes
#print(rolxwinMID)

"""

GRAFICACIONES

"""

# datos basicos
fig,ax = plt.subplots(2, figsize=(10,10))
# tipo de champs en cada linea
fig2,ax2 = plt.subplots(5,figsize=(10,10))
# tipo de champs en cada linea histogramas
fig3,ax3 = plt.subplots(6,figsize=(10,10))

axrol = ax[0]
axclases = ax[1]

axrolxclase_ADC = ax2[0]
axrolxclase_SUP = ax2[1]
axrolxclase_MID = ax2[2]
axrolxclase_TOP = ax2[3]
axrolxclase_JG = ax2[4]


hist_winTOT = ax3[0]
hist_winMID = ax3[1]
hist_winTOP = ax3[2]
hist_winADC = ax3[3]
hist_winSUP = ax3[4]
hist_winJG = ax3[5]

#ban.plot()
#win.plot()
axclases.bar(clases['Class'], clases['No de champs']) #cant de champs en cada clase
axrol.bar(roles['Role'], roles['No de champs']) # cnt de champs en cada rol

#LABELS PARA LAS PASTEL
labelsADC = list(adc['Class'])
labelsSUP = list(sup['Class'])
labelsMID = list(mid['Class'])
labelsTOP = list(top['Class'])
labelsJG = list(jg['Class'])

axrolxclase_ADC.pie(adc['No de champs'] , labels = labelsADC , autopct = '%1.1f%%')
axrolxclase_ADC.set_title('ADC')

axrolxclase_SUP.pie(sup['No de champs'] , labels = labelsSUP , autopct = '%1.1f%%')
axrolxclase_SUP.set_title('SUPPORT')

axrolxclase_MID.pie(mid['No de champs'] , labels = labelsMID , autopct = '%1.1f%%')
axrolxclase_MID.set_title('MID')

axrolxclase_TOP.pie(top['No de champs'] , labels = labelsTOP , autopct = '%1.1f%%')
axrolxclase_TOP.set_title('TOP')

axrolxclase_JG.pie(jg['No de champs'] , labels = labelsJG , autopct = '%1.1f%%')
axrolxclase_JG.set_title('JUNGLE')


hist_winTOT.hist(win) # cant de veces q se repite un winrate x champ hist de winrate
hist_winTOT.set_title('TEST')

#hist_winMID.hist(rolxwinMID[(rolxwinJG >= 50.03)]) todos los mids con winrate mayor a la media

hist_winMID.hist(rolxwinMID)
hist_winTOP.hist(rolxwinTOP)
hist_winADC.hist(rolxwinADC)
hist_winSUP.hist(rolxwinSUP)
hist_winJG.hist(rolxwinJG)

"""

ESTADISTICAS

"""

print('MEDIA WIN % TOTAL:')
print(np.mean(win))
print('DISTRIBUCION WIN % TOTAL:')
print(np.std(win))

print('MEDIA EN MID:')
print(np.mean(rolxwinMID))
print('DISTRIBUCION WIN % MID:')
print(np.std(rolxwinMID))

print('MEDIA EN TOP:')
print(np.mean(rolxwinTOP))
print('DISTRIBUCION WIN % TOP:')
print(np.std(rolxwinTOP))

print('MEDIA EN ADC:')
print(np.mean(rolxwinADC))
print('DISTRIBUCION WIN % ADC:')
print(np.std(rolxwinADC))

print('MEDIA EN SUP:')
print(np.mean(rolxwinSUP))
print('DISTRIBUCION WIN % SUP:')
print(np.std(rolxwinSUP))

print('MEDIA EN JG:')
print(np.mean(rolxwinJG))
print('DISTRIBUCION WIN % JG:')
print(np.std(rolxwinJG))

#tier de champ por linea comparamos con winrate

plt.show()