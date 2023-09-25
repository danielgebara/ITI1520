import math


# ITI1520
# Daniel Gebara
# 300401006
# Exercise d1


def tempsVoyage(distance,vitesse): 
    ''' (float,float) -> float '''
    return float(distance/vitesse*60)


def noteFinale(labos,devoirs,quiz,partiel,finale):
    ''' (float,float,float,float,float) -> float '''
    return(labos*0.1+devoirs*0.25+quiz*0.05+partiel*0.2+finale*0.4)


def bibformat(auteur, titre, ville, maisonEdition, annee):
    ''' str,str,str,str,int) -> str '''
    return auteur + " (" + str(annee) + "). " + titre + ". " + ville +": " + maisonEdition 


def bibformatPrint():
    ''' () -> None '''
    auteur = input("SVP entrer l'auteur: ")
    titre = input("SVP entrer le titre: ")
    ville = input("SVP entrer le ville: ")
    maisonEdititon = input("SVP entrer la maison d'edition: ")
    annee = input(str("SVP entrer l'annee: "))
    result = bibformat (auteur, titre, ville, maisonEdititon, annee)
    return result


def logFun(x):
    ''' (float) -> float '''
    y = (math.log10(x+3)) /4
    return y


def anneeBis(an):
    ''' (int) -> bool '''
    result = (an>1582)
    result = result and (an%4 == 0)
    result = result and (an%100 != 0) and not (an%400 == 0)
    return result
    # return ((an>1582 ) and an % 4 == 0 and an % 100 != 0 and not an % 400 == 0)

# Programme principal

