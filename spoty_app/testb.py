# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 18:12:57 2022

@author: waldo
"""
import testa
from importlib import reload
testa = reload(testa)


testa.reload(suma)
resultado  = testa.suma(5,3)
print(resultado)