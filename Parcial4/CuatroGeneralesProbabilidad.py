# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 18:30:57 2023

@author: Samuel García & Gabriela Lora
"""
import matplotlib.pyplot as plt
import numpy as np

def calcular_cumpleanos(n_personas):
    prob = 1.0
    for i in range(n_personas):
        prob *= (365 - i) / 365
    return 1 - prob

n_valores = np.arange(1, 81)
probabilidades = [calcular_cumpleanos(n) for n in n_valores]


plt.plot(n_valores, probabilidades, marker='o')
plt.xlabel('Número de prrsonas (n)')
plt.ylabel('Probabilidad de coincidencia de cumpleaños')
plt.title('Probabilidad de coincidencia de cumoleaños en un grupo de n personas')




