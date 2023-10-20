# ITI1520
# Daniel Gebara
# 300401006
# Exercise 6


def exercice6(s):
    '''(str) -> str'''
    mots = s.split()
    
    motsCodes = []
    
    for mot in mots:
        motCode = ''
        
        for i in range(0, len(mot), 2):
            if i + 1 < len(mot):
                motCode += mot[i + 1] + mot[i]
            else:
                motCode += mot[i]
        
        motsCodes.append(motCode)
    
    chaineCodee = ' '.join(motsCodes)
    
    return chaineCodee

# Programme principal
chaine = 'message secret'
chaineCodee = exercice6(chaine)
print(chaineCodee)  

chaine = 'Message'
chaineCodee = exercice6(chaine)
print(chaineCodee)  
