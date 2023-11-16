# ITI1520
# Daniel Gebara
# 300401006
# Exercice 2


def chercheM(matrice, v):
    NPas = 0  
    for i, ligne in enumerate(matrice):
        for j, element in enumerate(ligne):
            NPas += 1
            if element == v:
                print(f"Nombre de pas: {NPas}")
                return True  
    print(f"Nombre de pas: {NPas}")
    return False  

# Programme principal
M = [[1, 2, 10], [7, 5, 6], [8, 8, 9, 10]]
valeurRecherchee = 5

resultat = chercheM(M, valeurRecherchee)

print(resultat)