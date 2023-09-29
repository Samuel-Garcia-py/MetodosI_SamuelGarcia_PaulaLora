# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 15:04:16 2023

@author: GABI
"""

import sympy as sp

x, h, f = sp.symbols('x h f')



# Definir la función que quieres integrar
integrand = x * (x - h) * (x - 2 * h) * (x - 3 * h)

# Calcular la integral indefinida
integral = sp.integrate(integrand, x)

# Evaluar la integral en los límites de integración
result_en_b = integral.subs(x, 3 * h)
result_en_a = integral.subs(x, 0)

# Calcular el resultado de la integral definida
resultado = result_en_b - result_en_a

error=  resultado * (1/sp.factorial(4)* f**4)

# Imprimir el resultado en términos de h
print(error)