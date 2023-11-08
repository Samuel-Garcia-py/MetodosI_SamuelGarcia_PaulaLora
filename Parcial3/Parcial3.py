# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:01:18 2023

@author: GABI
"""

import numpy as np


def Jacobi(A,b,x0,itmax=5,tolerancia=1e-2):
    
    x = x0.copy()
    u = x.copy()
    sumk = x.copy()
    
    residuo = np.linalg.norm( np.dot(A,x) - b)
    
    print(residuo)
    
    it = 0
    
    while residuo >= tolerancia and it < itmax:
        
        
        u[:] = 0
        sumk[:] = 0.
        
        for i in range(A.shape[0]):
            for j in range(A.shape[1]):
                if i != j:
                    sumk[i] += A[i,j]*x[j]
            #print(sumk)
        
            u[i] = (b[i] - sumk[i])/A[i,i]
        
        
        x = u.copy()
        
        #print(x,residuo)
        # Norma infinita
        residuo = np.max(np.abs(np.dot(A,x) - b))
        # Norma griega
        #residuo = np.linalg.norm( np.dot(A,x) - b)
        
        it += 1
        
        if residuo > 1000:
            print('No calculable con Jacobi')
            x[:] = 0.
            break
        
    return x,it

A = np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2], [1,1,0,8,4],[0,-1,-2,4,700]])
b = np.array([1,2,3,4,5])
x0 = np.array([1,1,1,1,1])

np.linalg.solve(A,b)
Jacobi(A,b,np.array([0.,0.,0.,0.,0.]))

def GetT(A):
    
    M,N = A.shape
    
    D = np.zeros((M,N))
    R = D.copy()
    T = R.copy()
    
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if i == j:
              #  print(A[i,j])
               # print(1./A[i,j])
                D[i,j] = 1./A[i,j]
            else:
                R[i,j] = A[i,j]
    
 #   print(D)
 #   print(R)
    return np.dot(D,R)
T = GetT(A)
#print(Jacobi(A, b, x0))
Values,Vectors = np.linalg.eig(T)
np.abs(Values)
print (np.abs(Values))
