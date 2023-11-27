# ITI1520
# Daniel Gebara
# 300401006
# Exercice 3


class CompteBancaire:
    def __init__(self, nom='Dupont', solde=1000):
        self.nom = nom
        self.solde = solde

    def depot(self, somme):
        self.solde += somme

    def retrait(self, somme):
        if somme <= self.solde:
            self.solde -= somme
        else:
            print("Fonds insuffisants")

    def affiche(self):
        print(f"Titulaire: {self.nom}, Solde: {self.solde} euros")

    def __repr__(self):
        return f"CompteBancaire(nom={repr(self.nom)}, solde={repr(self.solde)})"

    def __eq__(self, other):
        return (
            isinstance(other, CompteBancaire) and
            self.nom == other.nom and
            self.solde == other.solde
        )
    
class CompteEpargne(CompteBancaire):
    def __init__(self, nom='Dupont', solde=1000, taux_interet_mensuel=0.3):
        super().__init__(nom, solde)
        self.taux_interet_mensuel = taux_interet_mensuel

    def changeTaux(self, valeur):
        self.taux_interet_mensuel = valeur

    def capitalisation(self, nombreMois):
        print(f"Nombre de mois : {nombreMois}, Taux d'intérêt mensuel : {self.taux_interet_mensuel}%")

        for mois in range(1, nombreMois + 1):
            interet = self.solde * (self.taux_interet_mensuel / 100)
            self.solde += interet

        print(f"Solde après capitalisation : {self.solde} euros")