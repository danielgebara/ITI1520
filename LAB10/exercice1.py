# ITI1520
# Daniel Gebara
# 300401006
# Exercice 1


class Temps:
    def __init__(self, heure, minute, seconde):
        self.setTemps(heure, minute, seconde)

    def setTemps(self, heure, minute, seconde):
        # les valeurs sont dans les intervalles corrects
        self.heure = heure % 24
        minute += heure // 24
        self.minute = minute % 60
        seconde += minute // 60
        self.seconde = seconde % 60

    def estAvant(self, t2):
        if self.heure < t2.heure or (self.heure == t2.heure and self.minute < t2.minute) or (self.heure == t2.heure and self.minute == t2.minute and self.seconde < t2.seconde):
            return True
        else:
            return False

    def durée(self, t2):
        # Calculer la différence entre les deux temps
        heures = t2.heure - self.heure
        minutes = t2.minute - self.minute
        secondes = t2.seconde - self.seconde

        if secondes < 0:
            secondes += 60
            minutes -= 1

        if minutes < 0:
            minutes += 60
            heures -= 1

        if heures < 0:
            heures += 24

        # Retourner un nouvel objet Temps avec la durée calculée
        return Temps(heures, minutes, secondes)

    def __str__(self):
        # Format
        return f"{self.heure}:{self.minute:02d}:{self.seconde:02d}"
    

# Exemple d'utilisation
temps1 = Temps(25, 10, 63)
print(temps1)

t1 = Temps(12, 4, 0)
t2 = Temps(10, 2, 1)

print(t1.estAvant(t2))  # False
print(t2.estAvant(t1))  # True

t2.setTemps(12, 45, 2)
print(t1.estAvant(t2))  # True

duree = t1.durée(t2)
print(duree)  # Affiche la durée entre t1 et t2