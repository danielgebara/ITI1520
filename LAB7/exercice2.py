# ITI1520
# Daniel Gebara
# 300401006
# Exercise 2


def histoN(t):
    ''' (tuple) -> dict '''
    # Crée un histogramme des occurrences de chaque nombre dans le tuple.
    g = {}
    i = 0
    while i < len(t):
        c = t[i]
        g[c] = g.get(c, 0) + 1
        i += 1
    return g

# Programme principal
t = (1, 2, -3, 3, 4, -3, 3, 3)
histogramme = histoN(t)
print(histogramme)
