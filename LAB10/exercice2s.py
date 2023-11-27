# ITI1520
# Daniel Gebara
# 300401006
# Exercice 2s


class Voiture:
    def __init__(self, marque='Ford', couleur='rouge', pilote='personne', vitesse=0):
        self.marque = marque
        self.couleur = couleur
        self.pilote = pilote
        self.vitesse = vitesse

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

# Exemple d'utilisation
voiture1 = Voiture()
voiture1.affiche_tout()  # Affiche les propriétés par défaut

voiture1.accelerer(1.3, 20)
voiture1.affiche_tout()  # Affiche les propriétés après accélération

voiture2 = Voiture(marque='Toyota', couleur='bleu', pilote='Bob', vitesse=30)
print(voiture2)  # Affiche les propriétés spécifiées

voiture3 = Voiture(marque='Toyota', couleur='bleu', pilote='Bob', vitesse=30)
print(voiture2 == voiture3)  # Test d'égalité entre deux objets Voiture
