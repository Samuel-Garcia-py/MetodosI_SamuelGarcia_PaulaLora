# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 18:26:53 2023

@author: Samuel García & Paula Lora
"""

import numpy as np
import sympy as sp

n= 2
x = sp.Symbol('x',real=True)
y = sp.Symbol('y',real=True)
def GetLaguerreRecursive(n,x):
    if n==0:
        poly = 1
    elif n==1:
        poly = 1-x
    else:
        poly = ((2*n-1-x) * GetLaguerreRecursive(n-1, x) - (n-1) * GetLaguerreRecursive(n-2, x))/n
    return sp.simplify(poly)

print (GetLaguerreRecursive(2,x))


# Usamos la fórmula de Rodriguez:
def Raices(n):
    Raices = []
    for n in range(1,3):
        laguerre = (sp.exp(x) / sp.factorial(n)) * (sp.diff(sp.exp(-x) * x**n, x, n))
       

    
        roots = sp.solve(laguerre, x)
        raices_reales = [root for root in roots if root.is_real and root >= 0]
    
        Raices.append(raices_reales)
    return Raices


print(Raices(n))  

Roots,Weights = np.polynomial.laguerre.laggauss(n)

def GetLaguerre(n,x,y):

    y = (sp.exp(-x)*x**3)
    
    poly = sp.exp(x)*sp.diff(y,x,n)/( np.math.factorial(n) )
    
    return poly
Laguerre = []

for i in range(n+1):
    
    Poly = GetLaguerre(i,x,y)
    Laguerre.append(Poly)
    
_x = np.linspace(0,10,100)


        
f1 = lambda x: (sp.exp(-x)*x*3)
Integral2 = np.sum( f1(Roots)*Weights )

print (Integral2)







