# ITI1520
# Daniel Gebara
# 300401006
# Exercise 3


def sommeDeTrois(t):
    ''' (tuple) -> bool '''
    # Vérifie si la somme de trois éléments consécutifs dans le tuple est égale à zéro.
    i = 0
    while i < len(t) - 2:
        if (t[i] + t[i + 1] + t[i + 2]) == 0:
            return True
        i += 1
    return False

# Programme principal
t = (1, 2, -3, 4, -1, 3)
resultat = sommeDeTrois(t)
print(resultat)