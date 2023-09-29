# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 23:37:04 2023

@author: Samuel García & Paula Lora
"""


# Este ejercicio nos pide usar la librería de sympy

import sympy as sp

# Para plantear la fórmula de Rodríguez necesitamos primero definir x. Sympay nos ayudó a 
# a definir la variable simbólica a través del comando symbols.
x = sp.symbols('x')

# Aquí vamos a almacenar las 20 raíces que me pide el ejercicio.
Raices = []

# Usamos la fórmula de Rodriguez:
for n in range(21):
    laguerre = (sp.exp(x) / sp.factorial(n)) * (sp.diff(sp.exp(-x) * x**n, x, n))
    
    
    # Aquí encontramos las raíces reales dentro del intervalo [0, infinito) y garantizamos que sean 
    # reales:
    
    roots = sp.solve(laguerre, x)
    raices_reales = [root for root in roots if root.is_real and root >= 0]
    
    # Almacena las raíces en la lista
    Raices.append(raices_reales)

# Imprime las raíces
for n, roots in enumerate(Raices):
    print(f"Raíces del polinomio de Laguerre L_{n}(x): {roots}")
