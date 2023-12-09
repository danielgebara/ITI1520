# ITI1520
# Mujtba Al-badri et Daniel Gebara
# Numero detudiant de Daniel: 300401006
# Numero detudiant de Mujtba: 300401141
# Devoir 5 


def triangle(n):
    ''' (int) -> None'''
    # case de base
    if n <= 0: 
        return 
    else: 
        triangle(n - 1) 
        for i in range(n):
            print('*', end='') 
        print()



def etoiles(n):
    '''(int) -> None '''
    if (n != 0): 
        # On affiche une ligne de n étoiles 
        for i in range(n): 
            print('*', end='') 
        print()
        # On affiche le diagramme plus petit 
        etoiles(n - 1) 
        for i in range(n): 
            print('*', end='') 
        print()


def prodListePos_rec(l, n):
    '''(list,int)-> int '''
    
    if (n == 0):
        return 1
    else:
         # Si l'élément actuel est positif, multipliez-le par le résultat de l'appel récursif
        if l[n-1] > 0:
            return prodListePos_rec(l, n-1) * l[n-1]
        else:
             # Si l'élément actuel n'est pas positif, faites simplement un appel récursif sans multiplication
            return prodListePos_rec(l, n-1)
        
def prodLRec1(l):
    ''' (list)-> int '''
    if not l:
        return 1
    else:
         # Calcule récursivement le produit des éléments positifs dans la liste
        produit = prodLRec1(l[:-1])
        # Si le dernier élément est positif, multipliez-le avec le résultat
        if l[-1] > 0:
            produit *= l[-1]
        return produit