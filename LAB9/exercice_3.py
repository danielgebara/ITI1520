# ITI1520
# Daniel Gebara
# 300401006
# Exercice 3


def compte(liste, v):
    NPas = 0  
    occurences = 0
    for element in liste:
        NPas += 1
        if element == v:
            occurences += 1

    print(f"Nombre de pas: {NPas}")
    return occurences

# Programme principal
l3 = [52, 14, 14, 8, 85, 69, 1, 77, 94, 96, 51, 65, 35, 32, 87, 92, 74, 47, 27,
      88, 11, 11, 26, 14, 100, 37, 62, 3, 63, 5, 20, 53, 28, 10, 43, 16, 94, 6, 82, 49,
      74, 55, 89, 97, 12, 38, 72, 94, 3, 77, 42, 26, 25, 16, 89, 10, 8, 63, 93, 77, 68,
      56, 74, 46, 54, 50, 80, 33, 69, 95, 2, 79, 73, 6, 31, 41, 38, 81, 88, 12, 39, 77,
      49, 30, 18, 22, 40, 40, 12, 51, 69, 32, 76, 77, 90, 60, 41, 12, 30, 65]

valeurRecherchee = 6

occurences = compte(l3, valeurRecherchee)

print(f"Nombre d'occurrences de {valeurRecherchee}: {occurences}")