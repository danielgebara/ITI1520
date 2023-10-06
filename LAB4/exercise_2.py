# ITI1520
# Daniel Gebara
# 300401006
# Exercise 2

def compteurN(n):
    ''' (int) -> None '''
    compteur = 1
    while(compteur <= n):
        print(compteur)
        compteur = compteur + 1


# Programme principal
# Demande a l'utilisateur d'entrer un nombre
n = int(input("SVP entrer un entier: "))
compteurN(n)




def compteurN(n):
    ''' (int) -> None '''
    for compteur in range(1, n + 1):
        print(compteur)


# Programme principal
# Demande a l'utilisateur d'entrer un nombre
n = int(input("SVP entrer un entier: "))
compteurN(n)