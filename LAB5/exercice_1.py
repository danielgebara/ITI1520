# ITI1520
# Daniel Gebara
# 300401006
# Exercice 1

def calculeMoyenne(l):
# Calcule la moyenne d'une liste
    ''' (list) -> float '''
    if len(l) == 0:
        return 0
    total = 0
    for index in l:
        total += index
        moyenne = total /len(l)
        return moyenne

i = input("Entrer une list separer par des espaces: ").split()
valeurs = [float(index) for index in i]
moyenne = calculeMoyenne(valeurs)
print ("La moyenne est: ", moyenne)
