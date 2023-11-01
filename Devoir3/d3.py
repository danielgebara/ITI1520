# ITI1520
# Daniel Gebara
# 300401006
# Exercise d3


def compte100(x):
    ''' (list) -> int '''
    # Cette fonction renvoie le nombre d'éléments dans la liste x qui sont strictement supérieurs à 100.
    return len([element for element in x if element > 100])


def sommeListeDiv2(x):
    ''' (list) -> int '''
    # Cette fonction renvoie la somme des éléments pairs de la liste x.
    return sum(element for element in x if element % 2 == 0)


def triples(chaine):
    ''' (str) -> bool '''
    # Cette fonction renvoie True si la chaîne contient trois caractères identiques consécutifs, sinon False.
    if len(chaine) < 3:
        return False  
    i = 0
    while i < len(chaine) - 2:
        if chaine[i] == chaine[i + 1] == chaine[i + 2]:
            return True  
        i += 1
    return False 


def momo(chaine):
    ''' (str) -> str '''
    # Cette fonction renvoie une chaîne compressée résultant de la compression de la chaîne d'entrée.
    if not chaine:
        return ""

    resultat = chaine[0]
    compte = 1
    i = 1

    while i < len(chaine):
        if chaine[i] == chaine[i - 1]:
            compte += 1
        else:
            resultat += str(compte) + chaine[i]
            compte = 1
        i += 1

    resultat += str(compte)

    return resultat


def noDup(chaine):
    ''' (str) -> str '''
    # Cette fonction renvoie une chaîne résultant de la suppression des caractères consécutifs en double dans la chaîne d'entrée.
    if not chaine:
        return ""

    resultat = chaine[0]
    i = 1

    while i < len(chaine):
        if chaine[i] != chaine[i - 1]:
            resultat += chaine[i]
        i += 1

    return resultat


# Programme principal

# test Q1
print(compte100([1, 102, -3.5, 104]))
print(compte100([1, 99, -3.5, -7]))
print(compte100([]))

# test Q2
print(sommeListeDiv2([1, 4, 3, 8, 5]))
print(sommeListeDiv2([]))
print(sommeListeDiv2([4, -10, 7]))

# test Q3
print(triples("abc"))
print(triples("abbbcdeeggggg"))
print(triples("abc2eee"))
print(triples("a23xxxxx"))
print(triples("abaacd"))

# test Q4
print(momo("a"))
print(momo("aabbbccccx"))
print(momo("aaa1111"))
print(momo("aaabcaax"))

# test Q5
print(noDup("a"))
print(noDup("aabbbccccx"))
print(noDup("aaa1111"))
print(noDup("aaabcaax"))