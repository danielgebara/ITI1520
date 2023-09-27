# ITI1520
# Daniel Gebara
# 300401006
# Exercise 2


def dowsLake(temp):
    '''(float) -> int'''
    if(temp>=80.0):
        return 1
    elif(60.0<=temp<80.0):
        return 2
    elif(40.0<=temp<60.0):
        return 3
    elif(temp<40.0):
        return 4
    
    
#Programme principal
temp = float(input("Quelle est la temperature?: "))
result = dowsLake(temp)
if result == 1:
    print("Natation")
elif result == 2:
    print("Soccer")
elif result == 3:
    print("Volleyball")
elif result == 4:
    print("Ski")
