# ITI1520
# Daniel Gebara
# 300401006
# Exercise 3


s = ''' En 1815, M. Charles-François-Bienvenu Myriel était évêque de
Digne. C’était un vieillard d’environ soixante-quinze ans ; il occupait le
siège de Digne depuis 1806. … '''

nombreS = s.replace('.', ' ').replace(',', ' ').replace(';', ' ').replace('\n', ' ')

nombreS = nombreS.strip()

nombreS = nombreS.lower()

nDe = nombreS.count('de')

nombreS = nombreS.replace('était', 'est')

print(nombreS)
print("Nombre de fois où s contient 'de':", nDe)


