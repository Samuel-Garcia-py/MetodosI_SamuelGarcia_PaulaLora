# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 14:12:30 2023

@author: GABI
"""

import numpy as np
import sympy as sp
from math import sqrt

x = sp.Symbol('x',real=True)
y = sp.Symbol('y',real=True)

def funcion(x):
    return ((x**2)*(4*x**2)*np.exp(-x**2)/(2* (sqrt(np.pi))))

def GetHermiteRecursive(n,x):
    if n==0:
        poly = 1
    elif n==1:
        poly = 2*x
    else:
        poly = ((2*x)*GetHermiteRecursive(n-1,x))- (2*(n-1)*GetHermiteRecursive(n-2,x))
    return sp.simplify(poly)


# Para encontrar las raíces de los polinomios de Hermite utilizaremos el proceso de
# Newton-Rapson: 

def GetDHermite(n, x):
    Polinomio = GetHermiteRecursive(n, x)
    return sp.diff(Polinomio, x, 1)


def GetNewton(f, df, x_n, itmax= 10000, precision = 1e-14):
    error = 1
    it = 0
    while error >= precision and it < itmax:
        try:
            x_n1 = x_n - f(x_n)/df(x_n)
            error = np.abs(f(x_n)/df(x_n))
        except ZeroDivisionError:
            print ('Zero Division')
        x_n = x_n1
        it += 1
        
    if it == itmax:
        return False
    else:
        return x_n
        
def GetRoots(f, df, x, tolerancia = 10):
    Roots = np.array([])
    for i in x:
        Root = GetNewton(f, df, i)
        if type(Root) != bool:
            Croot = np.round(Root, tolerancia)
            if Croot not in Roots:
                Roots = np.append(Roots, Croot)
    Roots.sort()
    
    return Roots

def GetAllRootsGHer(n):
    x_n = np.linspace(-np.sqrt(4*n+1),np.sqrt(4*n+1), 100)
    
    Hermite = []
    DHermite = []
    
    for i in range(n+1):
        Hermite.append(GetHermiteRecursive(i, x))
        DHermite.append(GetDHermite(i, x))
        
    polinomio = sp.lambdify([x], Hermite[n], 'numpy')
    Dpolinomio = sp.lambdify([x], DHermite[n], 'numpy')
    Roots = GetRoots(polinomio, Dpolinomio, x_n)
    
    if len(Roots) != n:
        ValueError('El numero de raices debe ser igual al n del polinomio')
        

    return Roots

""" se calculan los pesos de Hermite según la fórmula del taller"""

def GetweightsGHer(n):
    Roots = GetAllRootsGHer(n)

    Hermite_n = GetHermiteRecursive(n, x)
    Hermite_n_plus_1 = GetHermiteRecursive(n + 1, x)

    Weights = 2.0 / ((n + 1) * Hermite_n.subs(x, Roots) * Hermite_n_plus_1.subs(x, Roots))**2
    
    return Weights


roots= GetAllRootsGHer(1)
weights = GetweightsGHer(1)

resultado = np.sum(weights*funcion(roots))

print (resultado)