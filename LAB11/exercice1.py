# ITI1520
# Daniel Gebara
# 300401006
# Exercice 1


def check_digits(lst, size):
    # Cas de base
    if size == 0:
        return True
    
    # Vérifier si les chiffre sont entre 0 et 9
    if 0 <= lst[size - 1] <= 9:
        # Appel récursif avec une taille réduite
        return check_digits(lst, size - 1)
    else:
        return False
