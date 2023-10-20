# ITI1520
# Daniel Gebara
# 300401006
# Exercise 1


s1 = 'bon'
s2 = 'mauvais'
s3 = 'fou'

ou = 'ou' in s3
print("a) 'ou' est contenu en s3:", ou)

aucunEspace = ' ' not in s1
print("b) Un espace n'est pas contenu en s1:", aucunEspace)

concatenation = s1 + s2 + s3
print("c) La concaténation de s1, s2, et s3:", concatenation)

espace = ' ' in concatenation
print("d) L'espace est contenu dans la concaténation de s1, s2, et s3:", espace)

concatenation10 = s3 * 10
print("e) La concaténation de 10 copies de s3:", concatenation10)

caracteres = len(concatenation)
print("f) Le nombre total de caractères dans la concaténation de s1, s2, et s3:", caracteres)
