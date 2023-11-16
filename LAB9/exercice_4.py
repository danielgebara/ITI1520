# ITI1520
# Daniel Gebara
# 300401006
# Exercice 4


def compteOccurrences(matrice, v):
    NPas = 0  
    occurrences = 0
    for ligne in matrice:
        for element in ligne:
            NPas += 1
            if element == v:
                occurrences += 1

    print(f"Nombre de pas: {NPas}")
    return occurrences

# Programme principal
matrice = [[1, 2, 10], [7, 5, 6], [8, 8, 9, 10]]
valeurRecherchee = 5

occurrences = compteOccurrences(matrice, valeurRecherchee)

print(f"Nombre d'occurrences de {valeurRecherchee} dans la matrice : {occurrences}")
