# ITI1520
# Daniel Gebara
# 300401006
# Exercise d2


import math


def patinage(epaisseur,temperature):
    ''' (float,float) -> bool '''
    if (epaisseur >= 30 and temperature >= -10):
        return True
    else:
        return False
    

def alphaNote(note):
    ''' (int) -> str '''
    if (90 <= note <= 100):
        return 'A+'
    elif (85 <= note <= 89):
        return 'A'
    elif (80 <= note <= 84):
        return 'A-'
    elif (75 <= note <= 79):
        return 'B+'
    elif (70 <= note <= 74):
        return 'B'
    elif (65 <= note <= 69):
        return 'C+'
    elif (60 <= note <= 64):
        return 'C'
    elif (55 <= note <= 59):
        return 'D+'
    elif (50 <= note <= 54):
        return 'D'
    elif (40 <= note <= 49):
        return 'E'
    else:
        return 'F'
    

def alphaNoteVerif():
    ''' () -> None '''
    while True:
        valeur = float(input("SVP entrez la note finale (de 0 a 100): "))
        if (0 <= valeur <= 100):
            break
    result = alphaNote(valeur)
    print ("La note alphabetique est: ", result)
    if result in ['E', 'F']:
        print("Échoué")
    else:
        print("Réussi")

def boucles(n):
    ''' (int) -> None '''
    for i in range(1, n, 2):
        print(i)

    for i in range(n, 1, -2):
        print(i)


def facteursDeN(n):
    ''' (int) -> bool '''
    facteurs = []
    for i in range (2, n):
        if (n % i == 0):
            facteurs.append(i)
    if not facteurs:
        return False
    somme = sum(facteurs)
    print ("Les Facteurs de ", n, "= ", facteurs)
    print ("Somme des Facteurs = ", somme)
    return somme < n


def carreParfait(x):
    ''' (int) -> bool '''
    racine = math.sqrt(x)
    if (racine * racine == x):
        print (x, "est un carre parfait et sa racine carree est", racine)
        return True
    else:
        print (x, "n'est pas un carre parfait")
        return False
    

def maFun(n):
    ''' (int) -> float '''
    return (-1)**n / (2*n + 1)


def maFun_bis(n):
    ''' (int) -> float '''
    totale = 0
    for i in range(0,n):
        totale = totale + maFun(i)
    return 4 * totale


# Program principal

# Test Q1
print("Test Q1")
print(patinage(30, -10))
print(patinage(25.4, -15)) 
print(patinage(33, -15))
print(patinage(33, -5))

# Test Q2
print("Test Q2")
print(f"'{alphaNote(100)}'")
print(f"'{alphaNote(89)}'")
print(f"'{alphaNote(56)}'")
print(f"'{alphaNote(30)}'")

# Test Q4
print("Test Q4")
boucles(13)
boucles(10)

# Test Q5
print("Test Q5")
print(facteursDeN(12)) 
print(facteursDeN(9))
print(facteursDeN(5)) 

# Test Q6
print("Test Q6")
print(carreParfait(16))
print(carreParfait(15))

# Test Q7
print("Test Q7")
print(maFun(0)) 
print(maFun(1))
print(maFun(10))
print(maFun(2))

# Test Q8
print("Test Q8")
print(maFun_bis(10))
print(maFun_bis(100))
print(maFun_bis(1000))
print(maFun_bis(10000))