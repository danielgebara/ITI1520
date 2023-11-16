# ITI1520
# Daniel Gebara
# 300401006
# Exercice 1


import random

def cherche(liste, v):
    NPas = 0  
    for element in liste:
        NPas += 1
        if element == v:
            print(f"Nombre de pas: {NPas}")
            return True  
    print(f"Nombre de pas: {NPas}")
    return False  

# Programme principal
l3 = [7, 23, 86, 71, 17, 5, 63, 91, 69, 92, 76, 49, 22, 45, 39,
      52, 84, 51, 72, 28, 81, 52, 7, 50, 96, 64, 18, 71, 44, 46, 96,
      89, 31, 9, 31, 83, 80, 20, 17, 12, 97, 51, 90, 53, 25, 24, 6, 86,
      41, 2, 69, 26, 63, 9, 32, 91, 13, 33, 32, 96, 63, 10, 63, 63, 79,
      96, 82, 9, 70, 16, 84, 100, 55, 86, 22, 8, 2, 90, 91, 99, 15, 38,
      30, 7, 44, 8, 1, 8, 81, 86, 44, 44, 64, 2, 78, 96, 28, 80, 42, 44]

valeurRecherchee = 78

resultat = cherche(l3, valeurRecherchee)

print(resultat)