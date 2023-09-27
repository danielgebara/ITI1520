# ITI1520
# Daniel Gebara
# 300401006
# Exercise 4


def nombreRacine(a,b,c):
    ''' (float,float,float) -> str '''
    discriminant = b*2 - 4 * a * c
    if discriminant>0:
        return "Deux racines reelles distinctes"
    elif discriminant == 0:
        return "Une racine reelle"
    else:
        return "Aucun racines reelle"
    

# Programme principal
a = float(input("Entrer valeur a: "))
b = float(input("Entrer valeur b: "))
c = float(input("Entrer valeur c: "))
result = nombreRacine(a,b,c)
print("Il y a:", result)