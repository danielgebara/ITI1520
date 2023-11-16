# ITI1520
# Daniel Gebara
# 300401006
# Exercice 7


def triParInsertion(liste):
    NPas = 0  

    for i in range(1, len(liste)):
        valeurAInserer = liste[i]
        j = i - 1

        while j >= 0 and valeurAInserer < liste[j]:
            NPas += 1
            liste[j + 1] = liste[j]
            j -= 1

        liste[j + 1] = valeurAInserer

    print(f"Nombre de pas: {NPas}")

# Exemple d'utilisation
L = [3, 4, -1, 7, 2, 5, 16, -2, 17, 7, 82, -1]
triParInsertion(L)
print("Liste triée:", L)