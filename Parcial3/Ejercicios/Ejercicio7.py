# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:02:07 2023

@author: Samuel García
"""

import numpy as np

Itmax = 1000

#Sistema
A = np.array([[3., -1., -1.],
          [-1, 3, 1.],
          [2., 1., 4.],
          ])
# vector b
b = np.array([1., 3., 7.])

print("Sistema de ecuaciones: ")
for i in range(A.shape[0]):
    row = ["{0:3g}*x{1}".format(A[i, j], j + 1) for j in range(A.shape[1])]
    print("[{0}] = [{1:3g}]".format(" + ".join(row), b[i]))

x = np.zeros_like(b)


for it_count in range(1, Itmax):
    x_new = np.zeros_like(x)
    print("Iteración {0}: {1}".format(it_count, x))
    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x_new[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
    if np.allclose(x, x_new, rtol=1e-8):
        break
    x = x_new
    

    
    
    
    
    
    
    
    