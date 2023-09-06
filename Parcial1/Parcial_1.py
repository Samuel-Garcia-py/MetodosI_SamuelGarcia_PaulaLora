# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 17:02:11 2023

@author: Samuel García y Paula Lora
"""

                                   #Parcial 1

import math
import numpy as np

# Paso 1 definimos la función.
def Funcion(x):
    return (math.exp(-x)) - x

# Ahora que ya tenemos la función, hacemos la interpolación cuadrática de Newton.
    
def definir_x0_x1():
    x = np.linspace(-3, 5, 100)
    for i in x:
        evaluar= Funcion(i)
        if evaluar < 0:
            x0=evaluar
        if evaluar > 0:
            x1=evaluar
    x2= (x0 + x1) / 2 #Distancia entre los puntos.
    
    return x0, x1, x2


def interpolacion_cuadratica_newton(x, x0, x1, x2):
    
    f_x0 = Funcion(x0)
    f_x1 = Funcion(x1)
    f_x2 = Funcion(x2)
    
    #Hacemos la diferencia dividia:
    
    f_x0_x1 = (f_x1 - f_x0) / (x1 - x0)
    f_x0_x1_x2 = (f_x2 - f_x1) / (x2 - x1)
    
    resultado = f_x0 + f_x0_x1 * (x - x0) + f_x0_x1_x2 * (x - x0) * (x - x1)
    
    return resultado


# Una vez tenemos la expresión para la diferencia dividida, podemos transformarla a la fórmula 
# canónica así:

def forma_canonica_newton(x, x0, x1, x2):
    
    try:
        
        f_x0_x1_x2 = (Funcion(x2) - Funcion(x1)) / (x2 - x1)
        f_x0_x1 = (Funcion(x1) - Funcion(x0)) / (x1 - x0)
    
        a = f_x0_x1_x2
        b = f_x0_x1 - (x0 + x1) * f_x0_x1_x2
        c = Funcion(x0) - x0 * f_x0_x1 + x0 * x1 * f_x0_x1_x2
    
        return a, b, c
    
        
    
    except ZeroDivisionError:
        print('Error: División por cero')
        return None, None, None
    
    def calcular_x3(a, b, c, suma=True):
        
        discriminante = b**2 - 4*a*c
    
        if discriminante < 0:
            return None  # No hay raíces reales
    
        if suma:
            x3 = (-2 * c) / (b + math.sqrt(discriminante))
        else:
            x3 = (-2 * c) / (b - math.sqrt(discriminante))
            
        error = np.abs(Funcion(x3))
    
        print (x3)
        



x0, x1, x2 = definir_x0_x1()

if x0 is not None:
    print("x0 =", x0)
else:
    print("No se encontró x0.")

if x1 is not None:
    print("x1 =", x1)
else:
    print("No se encontró x1.")

if x2 is not None:
    print("x2 =", x2)
else:
    print("No se encontró x2.")

























