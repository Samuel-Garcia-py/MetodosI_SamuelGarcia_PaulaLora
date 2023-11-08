# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 13:58:07 2023

@author: Samuel García & Gabriela Lora
"""

# Punto 4 multiplicación de matrices:
    
import numpy as np

matriz1 = np.array([[1,0,0],[5,1,0],[-2,3,1]])
matriz2 = np.array([[4,-2,1],[0,3,7],[0,0,2]])

def multiplicar_matriz(matriz1, matriz2):
    if matriz1.shape[1] == matriz2.shape[0]:
        resultado = np.zeros((matriz1.shape[0], matriz2.shape[1]))  # Crear una matriz de ceros para el resultado
        for i in range(matriz1.shape[0]):
            for j in range(matriz2.shape[1]):
                for k in range(matriz1.shape[1]):
                    resultado[i][j] += matriz1[i][k] * matriz2[k][j]
        return resultado
    elif matriz1.shape[0] == matriz2.shape[1]:
        resultado = np.zeros((matriz1.shape[0], matriz2.shape[1]))  # Crear una matriz de ceros para el resultado
        for i in range(matriz1.shape[0]):
            for j in range(matriz2.shape[1]):
                for k in range(matriz1.shape[1]):
                    resultado[i][j] += matriz1[i][k] * matriz2[k][j]
        return resultado 
    else:
        print("Las matrices no se pueden operar.")


print("La respuesta es : ", multiplicar_matriz(matriz1, matriz2))

