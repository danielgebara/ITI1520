# ITI1520
# Daniel Gebara
# 300401006
# Exercise 1


def evalueAge(age):
    ''' (int) -> bool'''
    if (age >= 18) and (age <= 55):
        return True
    else:
        return False
    
    
#Programme principal
userAge= int(input("Entrer votre age: "))
if evalueAge(userAge):
    print("Transaction acceptee")
else:
    print("Transacation refusee")