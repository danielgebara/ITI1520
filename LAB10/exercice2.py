# ITI1520
# Daniel Gebara
# 300401006
# Exercice 2


class Voiture:
    pilote = 'personne'
    vitesse = 0
    def __init__(self, marque='Ford', couleur='rouge'):
        self.marque = marque
        self.couleur = couleur


    def choix_conducteur(self, nom):
        self.pilote = nom

    
    def accelerer(self, taux, duree):
        if self.pilote != 'personne':
            self.vitesse += taux * duree

    def affiche_tout(self):
        print(f"Marque: {self.marque}, Couleur: {self.couleur}, Pilote: {self.pilote}, Vitesse: {self.vitesse}")

    def __repr__(self):
        return f"Voiture(marque={repr(self.marque)}, couleur={repr(self.couleur)}, pilote={repr(self.pilote)}, vitesse={repr(self.vitesse)})"

    def __eq__(self, other):
        return (
            isinstance(other, Voiture) and
            self.marque == other.marque and
            self.couleur == other.couleur and
            self.pilote == other.pilote and
            self.vitesse == other.vitesse
        )

    def __str__(self):
        return f"Marque: {self.marque}, Couleur: {self.couleur}, Pilote: {self.pilote}, Vitesse: {self.vitesse}"

# Exemple d'utilisation
voiture1 = Voiture()
print(voiture1)  
voiture2 = Voiture(marque='Toyota', couleur='bleu')
print(voiture2)  # Affiche la marque et la couleur spécifiées, les autres attributs avec les valeurs par défaut

voiture1.choix_conducteur('Alice')
print(voiture1)  # Affiche la voiture avec le nouveau conducteur

voiture1 = Voiture()
voiture1.affiche_tout()  

voiture1.accelerer(1.3, 20)
voiture1.affiche_tout()  # Affiche les propriétés après accélération

voiture2 = Voiture(marque='Toyota', couleur='bleu', pilote='Bob', vitesse=30)
print(voiture2)  

voiture3 = Voiture(marque='Toyota', couleur='bleu', pilote='Bob', vitesse=30)
print(voiture2 == voiture3)  # Test d'égalité entre deux objets Voiture