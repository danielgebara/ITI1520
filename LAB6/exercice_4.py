# ITI1520
# Daniel Gebara
# 300401006
# Exercise 4


def compte(s, c):
    ''' (str, str) -> int '''
    count = 0
    i = 0
    while i < len(s):
        if s[i:i+len(c)] == c:
            count += 1
            i += len(c) - 1
        else:
            if s[i] == c:
                count += 1
        i += 1
    return count


def compte2():
    ''' (str, str) -> int '''
s = input("Entrez une chaîne de caractères : ")
nombreA = compte(s, 'a')
nombreDeLa = compte(s, 'de la')

print(f"Nombre de 'a' dans la chaîne : {nombreA}")
print(f"Nombre de 'de la' dans la chaîne : {nombreDeLa}")
