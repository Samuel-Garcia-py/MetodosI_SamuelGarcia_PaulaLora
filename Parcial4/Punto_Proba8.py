# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:47:07 2023

@author: GABI
"""

import numpy as np

N = 100000
contador=0
posibilidades_m1 = np.array([1,-1])
posibilidades_m2 = np.array([1,-1])
posibilidades_m3= np.array([1,-1])
posibilidades_m4= np.array([1,-1])
for i in range(N):
    np.random.shuffle(posibilidades_m1)
    np.random.shuffle(posibilidades_m2)
    np.random.shuffle(posibilidades_m3)
    np.random.shuffle(posibilidades_m4)
    m1= np.random.choice(posibilidades_m1)
    m2= np.random.choice(posibilidades_m2)
    m3= np.random.choice(posibilidades_m3)
    m4= np.random.choice(posibilidades_m4)
    if (m1+m2+m3+m4==0):
        contador +=1

probabilidad= contador/N


print("La probabilidad de obtener dos caras y dos sellos es:", probabilidad)
