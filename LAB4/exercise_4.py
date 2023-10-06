# ITI1520
# Daniel Gebara
# 300401006
# Exercise 4

def calculeFact(n):
# Fait le calcule et verifie les donnees
    ''' (int) -> int '''
    if (n == 0):
        return 1
    else:
        nombre = 1
        i = 1
        while(i <= n):
            nombre *= i
            i += 1
        return nombre


# Programme principal
# Prends les nombre et affiche des messages de verification
n = -1
while n < 0:
    n = int(input("SVP entrez un nombre positif: "))
    if n < 0:
        print("Le nombre doit être positif")

calcule = calculeFact(n)
print(f"{n}! =", calcule)