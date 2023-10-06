# ITI1520
# Daniel Gebara
# 300401006
# Exercise 3

import random

def devine():
# Choisi un nombre "Random" et dit si ses trop haut ou petit et devine encore
    ''' () -> int '''
    reponse = random.randint(0,10)
    essaye = 1
    while True:
        n = int(input("Deviner un nombre entre 1-10: "))
        if ( n == reponse):
            print ("BRAVO!, vous avez pris ", essaye , "essaye")
            return essaye
        elif (n <= reponse):
            print ("Trop bas!")
        else: 
            print ("Trop haut!")
        essaye = essaye + 1
            

# Programme principale
devine()


