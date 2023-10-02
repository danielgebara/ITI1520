# ITI1520
# Daniel Gebara
# 300401006
# Exercise 3


# Programme verifie si la valeur est divisuble par 2 et 3, 2 ou 3 et retourne (int)
def estDivisible(x):
    ''' (int) -> int '''
    if (x % 3 == 0 and x % 2 == 0 ):
        return 1
    elif (x % 3 == 0 or x % 2 == 0 ):
        return 2
    elif (x % 3 != 0 or x % 2 != 0 ):
        return 0
    

# Programme principal
# L'utilisateur donne un entire positif (int)
x = int(input("Entrer un entier positif: "))
result = estDivisible(x)
if result == 1:
    print("Nombre est divisble.")
elif result == 2:
    print("Nombre est divisble par 2 ou par 3.")
elif result == 0:
    print("Nombre est pas divisble.")