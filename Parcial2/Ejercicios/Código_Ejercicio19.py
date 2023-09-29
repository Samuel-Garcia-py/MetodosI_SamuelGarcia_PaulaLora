# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:35:21 2023

@author: samue
"""
import sympy as sp
import numpy as np

x = sp.Symbol('x', real = True)
y = sp.Symbol('y', real = True)
TD = 300
N_0V = 0.3
a = -1
b = 1
n = 50

def Integral(T, DT, x):
    return (np.tanh(np.sqrt(x**2 + DT**2)) * (T / (2 * T))) / (2 * np.sqrt(x**2 + DT**2))

def GetLaguerreRecursive(n,x):
    if n==0:
        poly = 1
    elif n==1:
        poly = 1-x
    else:
        poly = ((2*n-1-x) * GetLaguerreRecursive(n-1, x) - (n-1) * GetLaguerreRecursive(n-2, x))/n
    return sp.simplify(poly)


# Para encontrar las raíces de los polinomios de Laguerre utilizaremos el proceso de
# Newton-Rapson: 

def GetDLaguerre(n, x):
    Polinomio = GetLaguerreRecursive(n, x)
    return sp.diff(Polinomio, x, 1)


def Getnewton_rhapson(f, df, x_n, itmax= 10000, precision = 1e-14):
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
        Root = Getnewton_rhapson(f, df, i)
        if type(Root) != bool:
            Croot = np.round(Root, tolerancia)
            if Croot not in Roots:
                Roots = np.append(Roots, Croot)
    Roots.sort()
    
    return Roots

def GetallRootGLag(n):
    x_n = np.linspace(0, n + ((n-1)*np.sqrt(n)), 100)
    
    Laguerre = []
    DLaguerre = []
    
    for i in range(n+1):
        Laguerre.append(GetLaguerreRecursive(i, x))
        DLaguerre.append(GetDLaguerre(i, x))
        
    polinomio = sp.lambdify([x], Laguerre[n], 'numpy')
    Dpolinomio = sp.lambdify([x], DLaguerre[n], 'numpy')
    Roots = GetRoots(polinomio, Dpolinomio, x_n)
    
    if len(Roots) != n:
        ValueError('El numero de raices debe ser igual al n del polinomio')
        
    return Roots

""" se calculan los pesos de Laguerre según la fórmula del taller"""

def GetweightsLag(n):
    
    Roots = GetallRootGLag(n)
    weights = []
    for i in range (n):
        LagRoot= GetLaguerreRecursive(n+1, Roots[i])

        weight = Roots[i]/(((n+1)**2)*LagRoot**2)
        weights.append(weight)
    
    return weights

# Para variar DT:

for i in range(1, 20, 10e-4):
    DT = i
    T = 300
    x = sp.symbol('x', real = True)
    if Integral(T, DT, x) == 0:
        Temp_critica = 0
    else:
        None























