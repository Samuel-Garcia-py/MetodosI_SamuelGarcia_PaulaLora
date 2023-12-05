# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:41:55 2023

@author: Samuel García y Gabriela Lora
"""

import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output
import time
import copy
from tqdm import tqdm

#                                          Cosas de la Red Neuronal

sigmoide = lambda x: 1/(1+np.exp(-x))

class Capa:
    
    def __init__(self, NC, NN, FuncAct, tasa=0.1): # Juega con la tasa de mutación
        
        self.NC = NC
        self.NN = NN
        self.FuncAct = FuncAct
        self.tasa = tasa
        self.Pasos = 0
        
        self.W = np.random.uniform( -10.,10.,(self.NC,self.NN) )
        self.b = np.random.uniform( -10.,10.,(1,self.NN) )
        
    def Activacion(self, x):
        z = np.dot(x, self.W) + self.b
        return self.FuncAct( z )[0]
    
    def Mutar(self):
        self.W += np.random.uniform( -self.tasa, self.tasa, size=(self.NC,self.NN))
        self.b += np.random.uniform( -self.tasa, self.tasa, size=(1,self.NN))

def ObtenerCerebro():
    l0 = Capa(1, 5, sigmoide)
    l1 = Capa(5, 1, sigmoide)
    #l2 = Capa(2, 1, sigmoide)
    Cerebro = [l0, l1]
    return Cerebro

#                                     Estructura del Individuo

class Robot:
    
    def __init__(self, dt, Capas, Id=0):
        
        self.Id = Id
        self.dt = dt
        
        self.r = np.random.uniform([0.,0.])
        theta = 0.
        self.v = np.array([1.*np.cos(theta), 1.*np.sin(theta)])
        
        # Capacidad o aptitud del individuo
        self.Aptitud = np.inf
        self.Pasos = 0

        # Cerebro
        self.Capas = Capas
        
    def ObtenerR(self):
        return self.r
    
    def Evolucion(self):
        self.r += self.v * self.dt  # Integración de Euler 
        # Incrementar Pasos solo si el robot está dentro de la región de interés
        if -0.8 <= self.r[0] <= 0.8:
            self.Pasos += 1

        # Verificar si la red neuronal debe cambiar el vector de velocidad
        activacion = self.ActivacionCerebro(self.r[0])
        if activacion > 0.7:
            self.v = -self.v
            # Penalizar la activación excesiva disminuyendo Pasos
            self.Pasos *= 0.9  # Ajustar el factor según sea necesario

        # Cada generación devolvemos al robot al origen
        # Y estimamos su aptitud nuevamente
    def Reiniciar(self):
        self.Pasos = 0.
        self.r = np.array([0., 0.])
        self.Aptitud = np.inf

    # Aquí debes definir lo que significa mejorar en tu proceso evolutivo.
    def EstablecerAptitud(self):
        # La aptitud se define como el inverso del número de pasos
        self.Aptitud = 1 / (self.Pasos + 1)  # Se suma 1 para evitar la división por cero

        # Cosas del Cerebro
    def ActivacionCerebro(self, x, umbral=0.7):
        # ¡El umbral cerebral está a tu gusto!
        # cerca de 1 es exigente
        # cerca de 0 es síndrome de Down

        # Pase hacia adelante - la información fluye a través del modelo hacia adelante
        for i in range(len(self.Capas)):
            if i == 0:
                salida = self.Capas[i].Activacion(x)
            else:
                salida = self.Capas[i].Activacion(salida)

        self.Activacion = np.round(salida, 4)

        # Cambiamos el vector de velocidad
        if self.Activacion[0] > umbral:
            self.v = -self.v

            # Deberías penalizar de alguna manera, ¡ya que una activación demasiado alta es agotadora!
            # Para cualquier cerebro

        return self.Activacion

    # Aquí mutamos (cambiamos parámetros) para poder "aprender".
    def Mutar(self):
        for i in range(len(self.Capas)):
            self.Capas[i].Mutar()

    # Devolvemos la red neuronal ya entrenada
    def ObtenerCerebro(self):
        return self.Capas

    def Adelante(self):
        # Pase hacia adelante a través de la red neuronal
        activacion = self.ActivacionCerebro(self.r[0])
        # Si la activación es mayor que 0.7, invertir el vector de velocidad
        if activacion > 0.7:
            self.v = -self.v

def ObtenerRobots(N):
    
    Robots = []
    
    for i in range(N):
        Cerebro = ObtenerCerebro()
        r = Robot(dt, Cerebro, Id=i)
        Robots.append(r)
        
    return Robots

dt = 0.1
t = np.arange(0., 1., dt)
Robots = ObtenerRobots(10)

def ObtenerGrafico():
    
    fig = plt.figure(figsize=(8, 4))
    ax = fig.add_subplot(1, 2, 1)
    ax1 = fig.add_subplot(1, 2, 2)
    
    ax.set_xlim(-1., 1.)
    ax.set_ylim(-1., 1.)
 
    return ax, ax1

#                                           Evolución en el Tiempo

def EvolucionTemporal(Robots, e, Grafico=True):
    
    for it in range(t.shape[0]):
        
        if Grafico:
        
            clear_output(wait=True)
        
            ax, ax1 = ObtenerGrafico()
            ax1.set_ylim(0., 1.)
        
            ax.set_title('t = {:.3f}'.format(t[it]))
        
        Activacion = np.zeros(len(Robots))
        
        for i, p in enumerate(Robots):
            p.Evolucion()
         
            # Activación cerebral
            Act = p.ActivacionCerebro(p.ObtenerR()[0])
            Activacion[i] = Act
            # Región donde aumentamos los pasos para la aptitud
            
                
            if Grafico and i < 5: # Solo pintamos los primeros 5, debido al tiempo de cálculo
                ax.scatter(p.r[0], p.r[1], label='Id: {}, Pasos: {:.0f}'.format(p.Id, p.Pasos))
                ax.quiver(p.r[0], p.r[1], p.v[0], p.v[1])
                
        # Pintamos las activaciones de los primeros 5
        
        if Grafico:
            ax1.plot(np.arange(0, len(Robots[:5]), 1), Activacion[:5], marker='o', color='b', label='Activación')
            ax1.axhline(y=0.7, color='r')
        
        if Grafico:
        
            ax.legend(loc=0)  
            ax1.legend(loc=0)
            plt.show()
            time.sleep(0.001)
            
#                                                       Algoritmo Evolutivo

# Definimos la rutina de entrenamiento
def Genetico(Robots, epocas=200):
    VectorAptitud = np.array([])
    N = int(0.7 * len(Robots))
    
    for e in range(epocas):
        for p in Robots:
            p.Mutar()
            p.Reiniciar()
        
        EvolucionTemporal(Robots, e)
        
        for p in Robots:
            p.EstablecerAptitud()

        # Seleccionar los individuos más aptos
        puntuaciones = [(p.Aptitud, p) for p in Robots]
        puntuaciones.sort(key=lambda x: x[0], reverse=False)

        # Hacer una copia profunda de los objetos
        Temp = copy.deepcopy([p[1] for p in puntuaciones[:N]])

        # Actualizar la población con los individuos más aptos
        for i, r in enumerate(Robots):
            j = i % N
            Robots[i] = copy.deepcopy(Temp[j])

        # Registrar la mejor aptitud en esta época
        mejor_aptitud = puntuaciones[0][0]
        VectorAptitud = np.append(VectorAptitud, mejor_aptitud)

    # Devolver el robot más apto
    mejor_robot = puntuaciones[0][1]

    return mejor_robot

# Configurar la simulación
dt = 0.1
t = np.arange(0., 5., dt)
Robots = ObtenerRobots(200)  # Utiliza al menos 200 robots

# Ejecutar el algoritmo genético
Mejor = Genetico(Robots, epocas=200)

# Guardar los pesos de la mejor red neuronal
mejor_cerebro = Mejor.ObtenerCerebro()
np.save('mejores_pesos_cerebro.npy', [capa.W for capa in mejor_cerebro])

# Probar el modelo con los pesos guardados
pesos_cargados = np.load('mejores_pesos_cerebro.npy', allow_pickle=True)
cerebro_cargado = ObtenerCerebro()
for i, capa in enumerate(cerebro_cargado):
    capa.W = pesos_cargados[i]

# ... (realizar pruebas o evaluación adicional utilizando cerebro_cargado)




