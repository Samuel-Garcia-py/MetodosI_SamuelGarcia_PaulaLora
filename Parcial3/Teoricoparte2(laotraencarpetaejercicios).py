# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:01:18 2023

@author: GABI
"""

from __future__ import division, print_function
import numpy as np
import sympy as sp

# Definamos el sistema usando una lista
c = 700/10000
G = np.array([lambda x: (np.sin(x))**6 + c*(np.sin(x))**2 -c])

def GetF(G,r):
    
    n = r.shape[0]
    
    v = np.zeros_like(r)
    
    for i in range(n):
        v[i] = G[i](r[0])
        
    return v

def GetJacobian(f,r,h=1e-6):
    
    n = r.shape[0]
    
    J = np.zeros((n,n))
    
    for i in range(n):
        for j in range(n):
            
            rf = r.copy()
            rb = r.copy()
            
            rf[j] = rf[j] + h
            rb[j] = rb[j] - h
            
            J[i,j] = ( f[i](rf[0]) - f[i](rb[0])  )/(2*h)
            
    
    return J

def NewtonRaphson(G,r,itmax=1000,error=1e-9):
    
    it = 0
    d = 1.
    dvector = []
    
    while d > error and it < itmax:
        
        # Vector actual
        rc = r
        
        F = GetF(G,rc)
        J = GetJacobian(G,rc)
        InvJ = np.linalg.inv(J)
        
        r = rc - np.dot(InvJ,F)
        
        diff = r - rc
        
        d = np.max( np.abs(diff) )
        
        dvector.append(d)
        print(dvector)
        
        it += 1
    
    print(it)
    return r,dvector

r,dvector = NewtonRaphson(G,np.array([1.]))



