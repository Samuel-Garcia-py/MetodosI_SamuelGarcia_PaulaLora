# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 17:59:01 2023

@author: Samuel & Paula Lora
"""
import numpy as np
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt

#                     Ejercicio 7: Generalización del trapecio para integrales dobles


n = 100

# Con los dos siguientes linspace voy a generar los ejes de mi grilla

eje_x = np.linspace(-1,1,n+1)
eje_y = np.linspace(-1,1,n+1)

a = 0.
b = eje_x[-1]
R = 1

def ejes(eje_x,eje_y,R=1.):
    z = R**2 - eje_x**2 - eje_y**2
    if z <= 0.:
        return 0.
    else:
        return np.sqrt(z)
    
ejes = np.vectorize(ejes)
X,Y = np.meshgrid(eje_x,eje_y)
Z = ejes(X,Y)

# Ahora hago la figura:

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,Z, color = 'red')














