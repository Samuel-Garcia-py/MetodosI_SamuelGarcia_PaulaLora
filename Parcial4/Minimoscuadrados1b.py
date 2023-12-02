# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:00:07 2023

@author: Samuel García & Gabriela Lora
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


def func1(x,y):
  return 2*x - y - 2

def func2(x,y):
  return x + 2*y - 1

def func3(x,y):
  return x + y - 4


def distancia_minima(p):
  x, y = p
  return np.minimum(abs(func1(x,y)), abs(func2(x,y)), abs(func3(x,y)))


X,Y = np.meshgrid(np.arange(-5, 5, 0.01), np.arange(-5, 5, 0.01)) 


Z = distancia_minima((X,Y))


x_min, y_min = X[Z==Z.min()], Y[Z==Z.min()]
dist_min = Z.min()

print("La distancia mínima es:" + str({dist_min}))
print("x = " + str({x_min[0]}) + "y =" + str({y_min[0]}))


fig, ax = plt.subplots()
cp = ax.contourf(X, Y, Z)
fig.colorbar(cp)  
ax.set_title('Disrancia min')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot()



plt.show()

