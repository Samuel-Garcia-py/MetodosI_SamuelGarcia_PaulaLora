# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 20:44:32 2023

@author: Samuel García y Paula Lora 
"""

from IPython.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))

import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output
import time

#punto 12 inciso a NewtonRaphson
Ga = np.array([lambda  x,y:np.log(x**2+y**2)-np.sin(x*y)-np.log(2)-np.log(np.pi),
     lambda x,y: np.e**(x-y)+np.cos(x*y)
     ])

def GetFa(Ga,r):
    
    n = r.shape[0]
    
    v = np.zeros_like(r)
    
    for i in range(n):
        v[i] = Ga[i](r[0],r[1])
        
    return v
def GetJacobiana(f,r,h=1e-6):
    
    n = r.shape[0]
    
    J = np.zeros((n,n))
    
    for i in range(n):
        for j in range(n):
            
            rf = r.copy()
            rb = r.copy()
            
            rf[j] = rf[j] + h
            rb[j] = rb[j] - h
            
            J[i,j] = ( f[i](rf[0],rf[1]) - f[i](rb[0],rb[1]) )/(2*h)
            
    
    return J
def NewtonRaphsona(Ga,r,itmax=1000,error=1e-9):
    
    it = 0
    d = 1.
    dvector = []
    
    while d > error and it < itmax:
        
        # Vector actual
        rc = r
        
        F = GetFa(Ga,rc)
        J = GetJacobiana(Ga,rc)
        InvJ = np.linalg.inv(J)
        
        r = rc - np.dot(InvJ,F)
        
        diff = r - rc
        
        d = np.max( np.abs(diff) )
        
        dvector.append(d)
        print(dvector)
        
        it += 1
    
    print(it)
    return r,dvector

r,dvector = NewtonRaphsona(Ga,np.array([2.,2.]))


#punto 12 inciso a Desenso del gradiente 



G = np.array([lambda x,y,z: 6*x - 2*np.cos(y*z) - 1.,
     lambda x,y,z: 9*y + np.sqrt( x**2 + np.sin(z) + 1.06 ) + 0.9,
     lambda x,y,z: 60*z + 3*np.exp(-x*y)+10*np.pi - 3])

def GetFb(G,r):
    
    n = r.shape[0]
    
    v = np.zeros_like(r)
    
    for i in range(n):
        v[i] = G[i](r[0],r[1],r[2])
        
    return v
def GetJacobianb(f,r,h=1e-6):
    
    n = r.shape[0]
    
    J = np.zeros((n,n))
    
    for i in range(n):
        for j in range(n):
            
            rf = r.copy()
            rb = r.copy()
            
            rf[j] = rf[j] + h
            rb[j] = rb[j] - h
            
            J[i,j] = ( f[i](rf[0],rf[1],rf[2]) - f[i](rb[0],rb[1],rb[2])  )/(2*h)
            
    
    return J
def NewtonRaphsonb(G,r,itmax=1000,error=1e-9):
    
    it = 0
    d = 1.
    dvector = []
    
    while d > error and it < itmax:
        
        # Vector actual
        rc = r
        
        F = GetFb(G,rc)
        J = GetJacobianb(G,rc)
        InvJ = np.linalg.inv(J)
        
        r = rc - np.dot(InvJ,F)
        
        diff = r - rc
        
        d = np.max( np.abs(diff) )
        
        dvector.append(d)
        print(dvector)
        
        it += 1
    
    print(it)
    return r,dvector

r,dvector = NewtonRaphsonb(G,np.array([0.,0.,0.]))


#punto 12 Decesnso del gradiente

"""G=np.array ([lambda x,y:np.log(x**2+y**2)-np.sin(x*y)-np.log(2)-np.log(np.pi),
     lambda x,y: np.e**(x-y)+np.cos(x*y)
     ])
G1= np.array([lambda x,y,z: 6*x - 2*np.cos(y*z) - 1.,
     lambda x,y,z: 9*y + np.sqrt( x**2 + np.sin(z) + 1.06 ) + 0.9,
     lambda x,y,z: 60*z + 3*np.exp(-x*y)+10*np.pi - 3])

def GetF(G,r):
    
    n = r.shape[0]
    
    v = np.zeros_like(r)
    
    for i in range(n):
        v[i] = G[i](r[0],r[1],r[2])
        
    return v
GetF(G1,np.array([0.,0.,0.]))

def Metric(G,r):
    return 0.5*np.linalg.norm(GetF(G,r))**2
Metric(G1,np.array([1.,5.,1.]))

def GetJacobian(f,r,h=1e-6):
    
    n = r.shape[0]
    
    J = np.zeros((n,n))
    
    for i in range(n):
        for j in range(n):
            
            rf = r.copy()
            rb = r.copy()
            
            rf[j] = rf[j] + h
            rb[j] = rb[j] - h
            
            J[i,j] = ( f[i](rf[0],rf[1],rf[2]) - f[i](rb[0],rb[1],rb[2])  )/(2*h)
            
    
    return J

GetJacobian(G1,np.array([1.,5.,1.]))

def GetFig(R,M,it):
    
    fig = plt.figure(figsize=(6,3))
    
    ax = fig.add_subplot(1,2,1)
    ax1 = fig.add_subplot(1,2,2)
    
    ax.plot(R[:it])
    
    ax1.plot(M[:it])
   
    plt.show()
def Minimizer(G,r,lr=1e-2,epochs=int(1e4),error=1e-7):
    
    metric = 1
    it = 0
    
    M = np.array([])
    R = np.array([r])
    
    while metric > error and it < epochs:
        
        M = np.append(M,Metric(G,r))
        
        J = GetJacobian(G,r)
        Vector = GetF(G,r)
        
        # Machine learning
        r -= lr*np.dot(J,Vector)
        
        R = np.vstack((R,r))
        
        metric = Metric(G,r)
        
        it += 1
        
        if it%50 == 0:
            clear_output(wait=True)
            GetFig(R,M,it)
            print(r)
            time.sleep(0.001)
    
    return r

xsol = Minimizer(G,np.array([0.,0.,0.]),lr=1e-4)

G[2](xsol[0],xsol[1],xsol[2])"""