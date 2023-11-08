# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 22:55:29 2023

@author: Samuel García y Paula Lora 
"""
import sympy as sp

# Define las matrices SigmaX, SigmaY y SigmaZ
SigmaX = sp.Matrix([[0, 1], [1, 0]])
SigmaY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SigmaZ = sp.Matrix([[1, 0], [0, -1]])
Generadores= [SigmaX,SigmaY,SigmaZ]

# Definir el tensor de Levi-Civita εijk manualmente
epsilon = sp.Array([[[0, 0, 0], [0, 0, -1], [0, 1, 0]],[[0, 0, 1], [0, 0, 0], [-1, 0, 0]], [[0, -1, 0], [1, 0, 0], [0, 0, 0]]])

# Definir una constante compleja j
j = sp.I

# Verificar la relación del álgebra de Lie
for i in range(3):
    for j in range(i):
        commutator = SigmaX * Generadores[i] * Generadores[j] - SigmaX * Generadores[j] * Generadores[i]
        expected = 2 * j * epsilon[i, j, 0] * SigmaX + 2 * j * epsilon[i, j, 1] * SigmaY + 2 * j * epsilon[i, j, 2] * SigmaZ
        if not (commutator - expected).is_zero:
            print(f"La relación no se cumple para i = {i+1}, j = {j+1}.")
        else:
            print(f"La relación se cumple para i = {i+1}, j = {j+1}.")

