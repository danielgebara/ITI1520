# ITI1520
# Daniel Gebara
# 300401006
# Exercice 6


def triBulles(liste):
    NPas = 0  
    n = len(liste)

    for i in range(n):
        for j in range(0, n - i - 1):
            NPas += 1
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]

    print(f"Nombre de pas: {NPas}")

# Exemple d'utilisation
l1 = [64, 34, 25, 12, 22, 11, 90]
triBulles(l1)
print("Liste triée:", l1)
