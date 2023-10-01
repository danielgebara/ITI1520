# ITI1520
# Daniel Gebara
# 300401006
# Exercise 4


# Selon les valeurs calculer le discrimiant et retourne le nombre de racine (str)
def racineReelles(a,b,c):
    ''' (float,float,float) -> str '''
    discriminant = b**2 - 4 * a * c
    if (discriminant > 0):
        return "Il y a 2 racines"
    elif (discriminant == 0):
        return "Il y a 1 racine"
    elif (discriminant < 0):
        return "Aucun racine"
    

#Programme principal
# L'utilisateur entre les valeurs de a,b,c (float,float,float)
a = float(input("Entrer valeur a: "))
b = float(input("Entrer valeur b: "))
c = float(input("Entrer valeur c: "))
result = racineReelles(a,b,c)
print("Il y a:", result)

# Ca peut etre un erreur d'interpretation de python lorsquil arondit leur chiffres