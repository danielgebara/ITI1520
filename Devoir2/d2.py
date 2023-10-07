# ITI1520
# Daniel Gebara
# 300401006
# Exercise d2


def patinage(epaisseur,temperature):
    ''' (float,float) -> bool '''
    if (epaisseur >= 30 and temperature >= -10):
        return True
    else:
        return False
    

def alphaNote(note):
    ''' (int) -> str '''
    if (90 <= note <= 100):
        return 'A+'
    elif (85 <= note <= 89):
        return 'A'
    elif (80 <= note <= 84):
        return 'A-'
    elif (75 <= note <= 79):
        return 'B+'
    elif (70 <= note <= 74):
        return 'B'
    elif (65 <= note <= 69):
        return 'C+'
    elif (60 <= note <= 64):
        return 'C'
    elif (55 <= note <= 59):
        return 'D+'
    elif (50 <= note <= 54):
        return 'D'
    elif (40 <= note <= 49):
        return 'E'
    else:
        return 'F'
    

def alphaNoteVefif():
    ''' () -> None '''
# Not done
    result = alphaNote(note)
    while True:
        valeur = float(input("SVP entrez la note finale (de 0 a 100): "))
        if (0<= valeur <= 100):
            break
        else:
            print ("SVP entrez la note finale (de 0 a 100): ")
        print ("La note alphabetique est: ", result)


def boucles(n):
    ''' (int) -> None '''
    for i in range(1, n, 2):
        print(i)

    for i in range(n, 1, -2):
        print(i)


