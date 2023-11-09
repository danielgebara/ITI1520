def multiplicationMatrices(matriceA, matriceB): 
    # Ce programme multiplie 2 matrice et donne le resultat
    ''' (matrice, matrice) -> matrice '''
    if len(matriceA[0]) != len(matriceB): 
        raise ValueError("Les dimensions des matrices ne sont pas compatibles pour la multiplication.") 
    
    matriceResultat = [[0] * len(matriceB[0]) for _ in range(len(matriceA))] 
    for i in range(len(matriceA)): 
        for j in range(len(matriceB[0])): 
            for k in range(len(matriceB)): 
                matriceResultat[i][j] += matriceA[i][k] * matriceB[k][j] 
    return matriceResultat 

matriceA = [[1, 2, 3], [4, 5, 6]] 
matriceB = [[1, 2], [3, 4], [5,6]]
matriceProduit = multiplicationMatrices(matriceA, matriceB)

# Afficher le résultat 
print("Matrice A:") 
for row in matriceA:
    print(row) 
print("\nMatrice B:")
for row in matriceB:
    print(row)
print("\nProduit des matrices:")
for row in matriceProduit:
    print(row)