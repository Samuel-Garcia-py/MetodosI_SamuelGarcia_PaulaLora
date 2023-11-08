# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:14:40 2023

@author: Samuel Garcia y Paula Lora
"""

import sympy as sp
n = sp.diag(1, -1, -1, -1)
g0 = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
g1 = sp.Matrix([[0, 0, 0, -1], [0, 0, -1, 0], [0, 1, 0, 0], [1, 0, 0, 0]])
g2 = sp.Matrix([[0, 0, 0, -sp.I], [0, 0, sp.I, 0], [0, sp.I, 0, 0], [-sp.I, 0, 0, 0]])
g3 = sp.Matrix([[0, 0, -1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, -1, 0, 0]])
def anticonmutacion(a, b):
    return a * b + b * a
def anticonmutacion_g(u, v):
    return anticonmutacion(globals()["g" + str(u)], globals()["g" + str(v)])
for u in range(4):
    for v in range(u):
        x= anticonmutacion_g(u, v) == 2 * n[u, v] * sp.eye(4)

print(x)