# ITI1520
# Daniel Gebara
# 300401006
# Exercise 1


# Verifie l'age et retourn une valeur vrai ou faux (bool)
def evalueAge(age):
    ''' (int) -> bool '''
    if (age >= 18) and (age <= 55):
        return True
    else:
        return False
    

# Programme principal
# Demande l'age a l'utilisateur (int)
userAge= int(input("Entrer votre age: "))
if evalueAge(userAge):
    print("Transaction acceptee")
else:
    print("Transacation refusee")