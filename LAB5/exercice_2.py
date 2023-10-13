# ITI1520
# Daniel Gebara
# 300401006
# Exercice 2

def noteCalcule(l):
# Calcule la moyenne, la valeur maximal et la valeur minimal d'une liste
    ''' (list) -> float '''
    if len(l) == 0:
        return [0,0,0]
    
    somme = 0 
    max = l[0]
    min = l[0]


    for i in l:
        somme += i
        if i > max:
            max = i
        if i < min:
            min = i
    
    moyenne = somme / len(l)
    return [moyenne, max, min]

l = input("Entrer une list separer par des espaces: ").split()
l = [float(i) for i in l]
results = noteCalcule(l)
moyenne, max, min = results
print("Moyenne des notes: ", moyenne)
print("La valeur maximal est: ", max)
print("La valeur minimal est: ", min)


