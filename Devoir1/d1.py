def tempsVoyage(distance,vitesse): 
    ''' (float,float) -> float '''
    return float(distance/vitesse*60)


def noteFinale(a,b,c,d,e):
    ''' (float,float,float,float,float) -> float '''
    return(a*0.1+b*0.25+c*0.05+d*0.2+e*0.4)


def bibformat(auteur, titre, ville, maisonEdition, annee):
    ''' str,str,str,str,int) -> str '''
    return auteur, + " (" + str(annee) + "). " + titre + ". " + ville +": " + maisonEdition 

 
def bibformatPrint():
    ''' () -> '''
    return()


def logFun(x):


