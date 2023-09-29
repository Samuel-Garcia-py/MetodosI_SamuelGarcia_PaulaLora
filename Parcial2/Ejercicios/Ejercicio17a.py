# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:06:19 2023

@author: GABI
"""
import numpy as np
import sympy as sp


x = sp.Symbol('x',real=True)
y = sp.Symbol('y',real=True)
n=3


def Integrand_Func (x):
    return ((x**3)*(np.exp(x)-1)* (np.exp(-x)))/(np.exp(x)-2+(1/np.exp(x)))

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

Roots= GetallRootGLag(n)
Weights= GetweightsLag(n)

aproximacion= np.sum(Weights*Integrand_Func(Roots))

print (aproximacion)
