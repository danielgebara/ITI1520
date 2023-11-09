def transposeMatrice(matrice):
    # Ce programme arange la matrice en matrice 2d
    '''(matrice) -> matrice'''
    return [[matrice[j][i] for j in range(len(matrice))] for i in range(len(matrice[0]))]

matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriceTransposer = transposeMatrice(matrice)

for row in matriceTransposer:
    print(*row)