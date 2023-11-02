# Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

def donne_cartes(p):
    '''(list of str) -> tuple of (list of str, list of str)

    Retourne deux listes représentant les deux mains de cartes.
    Le donneur distribue une carte à l'autre joueur, une à lui-même,
    et cela continue jusqu'à la fin du paquet p.
    '''

    donneur = []
    autre = []

    for i, carte in enumerate(p):
        if i % 2 == 0:
            autre.append(carte)  # Distribue la carte au joueur 
        else:
            donneur.append(carte)  # Distribue la carte au donneur

    return (donneur, autre)


import random

def elimine_paires(l):
    '''
    (list of str) -> list of str

    Retourne une copie de la liste l avec toutes les paires éliminées 
    et mélange les éléments qui restent.

    (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
    >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
    ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
    >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
    ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    resultat = []

    # Crée un dictionnaire pour stocker le nombre de cartes de chaque valeur
    valeur_counts = {}
    
    for carte in l:
        valeur = carte[:-1]  # Obtient la valeur de la carte mais pas la couleur
        if valeur in valeur_counts:
            valeur_counts[valeur] += 1
        else:
            valeur_counts[valeur] = 1

    # Parcoure la liste d'origine et n'ajoute que les cartes qui ne forment pas de paires
    for carte in l:
        valeur = carte[:-1]
        if valeur_counts[valeur] % 2 != 0:
            resultat.append(carte)
        valeur_counts[valeur] -= 1

    random.shuffle(resultat)

    return resultat


def affiche_cartes(p):
    '''
    (list) -> None
    Affiche les éléments de la liste p séparés par des espaces
    '''
    for carte in p:
        print(carte, end=' ')
    print()  # met une ligne vide apres afficher toutes les cartes


def entrez_position_valide(n):
    '''
    (int) -> int
    Retourne un entier saisi au clavier, de 1 à n (1 et n inclus).
    Continue à demander si l'utilisateur entre un entier qui n'est pas dans l'intervalle [1, n].

    Précondition : n >= 1
    '''

    while True:
        try:
            position = int(input(f"Entrez un nombre entre 1 et {n}: ")) # Demande à l'utilisateur de saisir une position
            if 1 <= position <= n: # Vérifie si la position est dans l'intervalle valide
                return position # Retourne la position si elle est valide
            else:
                print(f"Le nombre doit être entre 1 et {n}. Réessayez.") # Affiche un message d'erreur si la position n'est pas valide
        except ValueError:
            print("Saisie invalide. Veuillez entrer un nombre valide.") # Gère les erreurs de saisie non numérique
     

def joue():
    '''()->None
    Cette fonction joue le jeu'''

    p = prepare_paquet()
    melange_paquet(p)
    tmp = donne_cartes(p)
    donneur = tmp[0]
    humain = tmp[1]

    print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
    print("Votre main est:")
    affiche_cartes(humain)
    print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
    print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
    attend_le_joueur()
    
    donneur = elimine_paires(donneur)
    humain = elimine_paires(humain)

    while True:
        affiche_cartes(humain)
        if len(humain) == 0:
            print("Vous n'avez plus de cartes. Vous gagnez !")
            break
        
        position = entrez_position_valide(len(humain))
        print(f"Vous défaussez : {humain[position - 1]}")
        del humain[position - 1]
        attend_le_joueur()
        
        affiche_cartes(donneur)
        if len(donneur) == 0:
            print("Je n'ai plus de cartes. Je gagne !")
            break
        
        position = random.randint(1, len(donneur))
        print(f"Je défausse : {donneur[position - 1]}")
        del donneur[position - 1]
        attend_le_joueur()

	 
# programme principale
joue()