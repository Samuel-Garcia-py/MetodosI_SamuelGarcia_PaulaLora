# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:06:24 2023

@author: GABI
"""

from scipy.optimize import minimize

P0 = [0, 0, 0]
def Funcion(xyz):
    x, y, z = xyz
    return x**2 + y**2 + z**2 - 2*z + 1


def restriccion_fun(xyz):
    x, y, z = xyz
    return 2*x - 4*y + 5*z - 2

resultado = minimize(Funcion, P0, constraints={'type': 'eq', 'fun': restriccion_fun})

print(f"Paramtros: {resultado.x}")
print(f"Mínimo: {resultado.fun}")
