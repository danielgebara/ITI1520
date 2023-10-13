# ITI1520
# Daniel Gebara
# 300401006
# Exercice 3

import math


def distanceLancer(v):
# Calcule la distance d'un lancer en utilisant les angles
    distances = []  
    for angle in range(0, 91, 10):
        ar = math.radians(angle)
        distance = (v**2 * math.sin(2*ar)) / 9.81
        distances.append(distance)
    return distances
distances = distanceLancer()
for angle, distance in zip(range(0, 91, 10), distances):
    print("Angle: ", {angle}, "Degres, Distance: " ,{distance:.2}, "metres")

