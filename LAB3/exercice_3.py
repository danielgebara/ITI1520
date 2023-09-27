# ITI1520
# Daniel Gebara
# 300401006
# Exercise 3


def estDivisible(x):
    ''' (int) -> int '''
    if (x % 3 == 0 and x % 2 == 0 ):
        return 1
    elif (x % 3 == 0 or x % 2 == 0 ):
        return 2
    elif (x % 3 != 0 or x % 2 != 0 ):
        return 0
    

x = int(input("Entrer un entier positif: "))
result = estDivisible(x)
if result == 1:
    print("Nombre est divisble par 2 et par 3.")
elif result == 2:
    print("Nombre est divisble par 2 ou par 3, mais pas les deux.")
elif result == 0:
    print("Nombre est pas divisble ni par 2 ni par 3")