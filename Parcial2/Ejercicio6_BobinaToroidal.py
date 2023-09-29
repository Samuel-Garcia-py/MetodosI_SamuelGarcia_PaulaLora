# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 17:14:55 2023

@author: Samuel García & Paula Lora
"""

import numpy as np


#                                   Ejercicio 6: Bobina toroidal:

# Solución con método del trapecio simple:

a = 0.01
b = -a
R = 0.5

n = 100

h = (b-a)/(n-1)

x = np.linspace(a, b, n)

f= (np.sqrt(a**2 - x**2)) / R + x


I_trap = abs((h/2)*(f[0] + 2 * sum(f[1:n-1]) + f[n-1]))
I_teo = (np.pi)*(R - np.sqrt(R**2 - a**2))

err_trap = (abs(I_trap - I_teo/I_teo))/100

print(I_trap)
print(I_teo)
print(err_trap)

















