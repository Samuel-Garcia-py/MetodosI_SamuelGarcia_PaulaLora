# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:43:20 2023

@author: Samuel García y Paula Lora
"""

import sympy as sp
import numpy as np 
x = sp.Symbol('x',real=True)
y = sp.Symbol('y',real=True)
n = 3

h = 6.626 * 10e-34
k = 1.3806 * 10e-23
c = 3* 10e8
T = 5772

lambda_0 = 100 * 1e-9
lambda_1 = 400 * 1e-9
v_1 = c / lambda_0
v_2 = c / lambda_1

# Con base a las constantes definimos los límites de integración:

a = (h*v_1) / (k * T)
b = (h*v_2) / (k * T)


Integrando = lambda x: (x**3)/ (np.exp(x) -1)

Roots, Weights = np.polynomial.legendre.leggauss(n)

resultado = np.sum(Weights * Integrando(Roots))

x = 0.5*( (b-a)*Roots + a + b )

Integral1 = 0.5*(b-a)*np.sum(Weights*Integrando(x))

print(Integral1)


Roots,Weights = np.polynomial.laguerre.laggauss(n)


def GetLaguerre(n,x,y):

    y = ((x**3)*(sp.exp(x)-1)* (sp.exp(-x)))/(sp.exp(x)-2+(1/sp.exp(x)))
    
    poly = sp.exp(x)*sp.diff(y,x,n)/( np.math.factorial(n) )
    
    return poly
Laguerre = []

for i in range(n+1):
    
    Poly = GetLaguerre(i,x,y)
    Laguerre.append(Poly)
    
_x = np.linspace(0,10,100)


        
f1 = lambda x: ((x**3)*(np.exp(x)-1)* (np.exp(-x)))/(np.exp(x)-2+(1/np.exp(x)))
Integral2 = np.sum( f1(Roots)*Weights )

#si colocas Integral1/Integral2 en la terminal si imprime un valor que es -3.608267347383836e-29

Resultado= Integral1/Integral2
