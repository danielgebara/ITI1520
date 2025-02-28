import math


# ITI1520
# Daniel Gebara
# 300401006
# Exercise d1


def tempsVoyage(distance,vitesse): 
# Calculer le temps du voyage en minutes
    ''' (float,float) -> float '''
    return float(distance/vitesse*60)


def noteFinale(labos,devoirs,quiz,partiel,finale):
# Calculer la moyenne finale de ton cours
    ''' (float,float,float,float,float) -> float '''
    return(labos*0.1+devoirs*0.25+quiz*0.05+partiel*0.2+finale*0.4)


def bibformat(auteur, titre, ville, maisonEdition, annee):
# La bonne format dossard
    ''' (str,str,str,str,int) -> str '''
    anneeS = str(annee)
    format = auteur + " (" + anneeS + "). " + titre + ". " + ville +": " + maisonEdition 
    return format


def bibformatPrint():
# Affiche les resultats selon les instructions demander
    ''' () -> None '''
    auteur = input("SVP entrer l'auteur: ")
    titre = input("SVP entrer le titre: ")
    ville = input("SVP entrer le ville: ")
    maisonEdititon = input("SVP entrer la maison d'edition: ")
    annee = input(str("SVP entrer l'annee: "))
    result = bibformat (auteur, titre, ville, maisonEdititon, annee)
    print (result)


def logFun(x):
# Entrer un entier positif (x) et resous l'equation, renvoie (y).
    ''' (float) -> float '''
    y = (math.log10(x+3)) /4
    return y


def anneeBis(an):
# Entrer un an qui est plus grand que (1582) et qui suit et respect les autres condition et retourne True ou False
    ''' (int) -> bool '''
    result = (an>1582)
    result = result and (an%4 == 0)
    result = result and (an%100 != 0) and not (an%400 == 0)
    return result


#Programe Principale
#Test 1
print(tempsVoyage(400,100))
print(tempsVoyage(20.6,60))
#Test 2
print(noteFinale(100,100,100,100,100))
print(noteFinale(50,90.5,60,80,70))
#Test 3
print(bibformat("Antoine de Saint Exupery", "Le petit prince", "Paris", "Jeunesse", 1943))
#Test 4
bibformatPrint()
#Test 5
print(logFun(7))
print(logFun(20))
print(logFun(999999997))
print(logFun(0.1))
print(logFun(9997))
#Test 6
print(anneeBis(1904))
print(anneeBis(1928))
print(anneeBis(1950))
print(anneeBis(1990))
print(anneeBis(1932))