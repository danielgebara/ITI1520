# ITI1520
# Daniel Gebara
# 300401006
# Exercice 2


def create_list_recursive(L, n):
    # Cas de base
    if n == 0:
        return L
    
    # Ajouter la valeur (n - 1) à la liste
    L.append(n - 1)
    
    # Appel récursif avec une valeur réduite de n
    return create_list_recursive(L, n - 1)
