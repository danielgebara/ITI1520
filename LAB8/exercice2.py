def sommeMatrices(matriceA, matriceB):
    # Ce programme additionne 2 matrice et donne le resultat
    ''' (matrice, matrice) -> matrice '''
    if len(matriceA) != len(matriceB) or len(matriceA[0]) != len(matriceB[0]): 
        raise ValueError("Les dimensions des matrices ne sont pas compatibles.")
    matriceResultat = [[a + b for a, b in zip(row_A, row_B)] for row_A, row_B in zip(matriceA, matriceB)]
    return matriceResultat 

matriceA = [[1, 2], [3,4]]
matriceB = [[1,1], [1,1]]
matriceSomme = sommeMatrices(matriceA, matriceB) 

# Afficher le résultat 
print("Matrice A:")
for row in matriceA: 
    print(row) 
print("\nMatrice B:")
for row in matriceB:
    print(row) 
print("\nSomme des matrices:") 
for row in matriceSomme: 
    print(row)