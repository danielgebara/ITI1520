# ITI1520
# Daniel Gebara
# 300401006
# Exercise 5


def exercice5(s):
    '''(str) -> str'''
    if len(s) < 2:
        return s  
    else:
        result = s[0]  
        for i in range(1, len(s)):
            result += ' ' + s[i]
        return result


# Programme principal
s = input("Entrez une chaîne de caractères : ")
resultat = exercice5(s)
print(resultat)