# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:25:53 2023

@author: Samuel Garcia y Paula Lora
"""

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

x = sym.symbols('x', real=True)
y= sym.symbols('y', real=True)

z0 = (-0.5 + np.sqrt(3)*sym.I/2)

z1 = (-0.5 - np.sqrt(3)*sym.I/2)

z = x + sym.I*y

f = z**3 - 1

F = [sym.re(f), sym.im(f)]

dxr = sym.diff(F[0], x)
dyr = sym.diff(F[0], y)
dxi = sym.diff(F[1], x)
dyi = sym.diff(F[1], y)

jn = sym.Matrix([[dxr, dyr], [dxi, dyi]])

Fn = sym.lambdify([x, y], F, "numpy")

def NewtonRaphson(z0, Fn, Jn, max_iter):
    z = z0
    for i in range(max_iter):
        F = Fn(sym.re(z), sym.im(z))
        Jacobiano = Jn.subs([(x, sym.re(z)), (y, sym.im(z))])
        JacobianoInv = Jacobiano.inv()
        deltaZ = -JacobianoInv @ sym.Matrix(F)
        z += deltaZ[0] + deltaZ[1]*sym.I
        if abs(F[1]-F[0]) < 1e-8:
            return z
    return None

raices = [-(1/2)+np.sqrt(3)*sym.I/2, -1, -(1/2)-np.sqrt(3)*sym.I/2]


N = 50
#N= 300
d = np.linspace(-1, 1, N)
r= np.linspace(-1, 1, N)

fractal = np.zeros((N,N), np.int64)

for i in range(N):
    for j in range(N):
        z0 = d[i] + sym.I*r[j]
        raiz = NewtonRaphson(z0, Fn, jn, 100)
        if abs(raiz - raices[0]) < 1e-3:
            fractal[i,j] = 20
        elif abs(raiz - raices[1]) < 1e-3:
            fractal[i,j] = 100
        elif abs(raiz - raices[2]) < 1e-3:
            fractal[i,j] = 255

print(z0)

plt.imshow(fractal, cmap='coolwarm' ,extent=[-1,1,-1,1])