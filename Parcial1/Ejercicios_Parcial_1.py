# -*- coding: utf-8 -*-
"""
Created on Tue Sep 5 21:56:47 2023

@author: Samuel García & Paula Lora
"""



                         # EJERCICIO 4 Interpolación de Lagrange

import urllib.request  
import pandas as pd 
import math
import numpy as np
from scipy.interpolate import lagrange

# Obtenemos la dirección del enlace:
URL = 'https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/Parabolico.csv'

nombre_archivo = "Trayectoria_Bala.csv"

urllib.request.urlretrieve(URL, nombre_archivo)  # Para descarcargar el archivo directamente de la web
Lista_trayectoria = pd.read_csv('Trayectoria_Bala.csv')

# A continuación, con el parámetro tolist se guarda los nombres de las columnas en dos listas:
x=Lista_trayectoria['X'].tolist()
y=Lista_trayectoria['Y'].tolist()

# Ahora que ya tenemos los puntos en las variables x y y, usamos el código de Lagrange para dos parámetros
# de la libreía spicy.
polinomio = lagrange(x, y) #Se interpola con Lagrange.

# La derivada de la interpolación (posición) es la v(t).
# Para hallar la velocidad incial usamos el hint
Vel_inicial = ((1 + np.polyder(polinomio)(0)**2)**0.5) / 0.1


# Como es un movimiento en x y en y, el ángulo se puede sacar con arco-tangente:
angulo = math.degrees(math.atan(np.polyder(polinomio)(0)))


print(f"La magnitud de la velocidad incial de la bala es {round(Vel_inicial,1)} m/s dirección {round(angulo,1)} °.")


                         # Ejercicio 3 Raíces de un Polinomio 

         # Calcular todas las raíces reales de f(x) = 3x^5 + 5x^4 - x^3
 
# Paso 1: Definimos la función.        
def function(x):
    return (3*(x**5)) + (5*(x**4)) - (x**3)

# Paso 2: Usando Linspace se crea un conjunto de dátos para el polinomio.
x = np.linspace(-1,1,50)
y = function(x)

# Paso 3: Derivamos la función.
def Derivative(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)

#Aplicamos el método de Newton-Rhapson
def GetNewtonMethod(Funcion,Derivada,xn,itmax=100,precision=1e-8):
    
    # Este método toma un xn y construye la ecuación de la recta usando la
    # derivada de f(x) en xn. 
    
    error = 1. 
    
    it = 0 # Las iteraciones comienzan en 0 y llegan hasta 100 según itmax.
    
    while error > precision and it < itmax:
        
        try:
            
            # Se pretende que el siguiente punto en la iteración 
            # sea un raíz de f(xn+1) = 0, por tanto:
            xn1 = xn - Funcion(xn)/Derivada(Funcion,xn)
            
            # Criterio de parada
            error = np.abs(Funcion(xn)/Derivada(Funcion,xn))
            
        except ZeroDivisionError:
            print('Division por cero')
            
        xn = xn1
        it += 1
        
   # print('Raiz',xn,it)
    
    if it == itmax:
        return False
    else:
        return xn 
    
def GetAllRoots(x, tolerancia=10):
    
    Raices = np.array([])
    
    for i in x:
        
        Raiz = GetNewtonMethod(function,Derivative,i)
        
        if Raiz != False:
            
            croot = np.round(Raiz, tolerancia)
            
            if croot not in Raices:
                Raices = np.append(Raices,croot)
                
    Raices.sort()
    
    return Raices

print(GetAllRoots(x))
    


