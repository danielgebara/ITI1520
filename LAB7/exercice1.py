# ITI1520
# Daniel Gebara
# 300401006
# Exercise 1


def creer_histogramme(chaine):
    ''' (str) -> dict '''
    # Crée un histogramme des caractères dans une chaîne.
    histogramme = {}
    i = 0

    while i < len(chaine):
        caractere = chaine[i]
        if caractere in histogramme:
            histogramme[caractere] += 1
        else:
            histogramme[caractere] = 1
        i += 1

    sorted_items = sorted(histogramme.items(), key=lambda x: x[0])
    j = 0

    while j < len(sorted_items):
        item = sorted_items[j]
        print(item[0], ":", item[1])
        j += 1

# Programme principal
chaine = "pythonprogramming"
creer_histogramme(chaine)

