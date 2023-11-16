# ITI1520
# Daniel Gebara
# 300401006
# Exercice 5


def rechercheBinaire(liste, v):
    NPas = 0  
    debut = 0
    fin = len(liste) - 1

    while debut <= fin:
        milieu = (debut + fin) // 2
        valeurMilieu = liste[milieu]

        NPas += 1

        if valeurMilieu == v:
            print(f"Nombre de pas: {NPas}")
            return True  
        elif valeurMilieu < v:
            debut = milieu + 1
        else:
            fin = milieu - 1

    print(f"Nombre de pas: {NPas}")
    return False  

# Exemples d'utilisation
resultat1 = rechercheBinaire([1, 2, 3, 4, 4, 5, 7, 9, 10, 13], 10)
print(resultat1)

resultat2 = rechercheBinaire([1, 2, 3, 4, 4, 5, 7, 9, 10, 13], 6)
print(resultat2)
