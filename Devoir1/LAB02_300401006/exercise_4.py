from math import sqrt
# ITI1520
# Daniel Gebara
# 300401006
# Exercise 4

def triangle(cote1,cote2,cote3):
# Calculer la surface d'une triangle
    ''' (float,float,float) -> float '''
# Calculer le perimetre
    p = cote1+cote2+cote3
# Calculer la surface 
    s = sqrt(p*(p-2*cote1)*(p-2*cote2)*(p-2*cote3))/4
    return s