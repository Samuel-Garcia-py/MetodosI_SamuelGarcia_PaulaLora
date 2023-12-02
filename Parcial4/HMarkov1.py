# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:08:55 2023

@author: GABI
"""

import numpy as np

PJ= np.array([0.5,0.5])
PB= np.array([0.9, 0.1])
priori = np.array([0.2, 0.8])

MatrizT = np.array([[0.8, 0.2], [0.2, 0.8]])
prob_cara_justa = 0.5
prob_cara_sesgada = 0.9
prob_sello_justa = 0.5
prob_sello_sesgada = 0.1

observaciones = np.array([0, 1, 1, 1, 0, 1, 0, 1])

N_obervaciones = len(observaciones)

viterbi = np.zeros((N_obervaciones, 2))
traceback = np.zeros((N_obervaciones, 2), dtype=int)

for t in range(N_obervaciones):
    for estado in range(2):
        if t == 0:
            viterbi[t, estado] = priori[estado] * (prob_cara_justa if observaciones[t] == 1 else prob_sello_justa)
        else:
            transiciones = viterbi[t - 1] * MatrizT[:, estado]
            max_transicion = np.max(transiciones)
            viterbi[t, estado] = max_transicion * (prob_cara_sesgada if observaciones[t] == 1 else prob_sello_sesgada)
            traceback[t, estado] = np.argmax(transiciones)

SecuenciaOculta = np.zeros(N_obervaciones, dtype=int)
EFinal = np.argmax(viterbi[-1])
SecuenciaOculta[-1] = EFinal

for t in range(N_obervaciones - 1, 0, -1):
    EFinal = traceback[t, EFinal]
    SecuenciaOculta[t - 1] = EFinal

print("Secuencia:")
print(SecuenciaOculta)
print("Probabilidad:")
print(np.max(viterbi[-1]))
