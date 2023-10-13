# ITI1520
# Daniel Gebara
# 300401006
# Exercice 4

import math


def calculeMoyenne(v):
# A partir de la list calcule l'ecart type et retourne le resultat
    ''' (list) -> float '''
    return sum(v) / len(v)

def ecartType(v):
    moyenne = calculeMoyenne(v)
    n = len(v)
    variance = 0

    for x in v:
        variance += (x - moyenne) ** 2
    variance /= n
    ecart_type = math.sqrt(variance)
    return ecart_type

v_input = input("Entrer une list separer par des espaces: ").split()
v_sqrt = v_input
v = [float(x) for x in v_sqrt]

deviation = ecartType(v)

print("la deviation est:", deviation)

