# ITI1520
# Daniel Gebara
# 300401006
# Exercice 3


def pgcd(x, y):
    # Cas de base: Si y est égal à 0, alors le PGCD est x
    if y == 0:
        return x
    
    # Appel récursif avec l'ordre échangé (y, x mod y)
    return pgcd(y, x % y)
