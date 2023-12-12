def maFonction4(L):
    p = 0
    for i in range(1,len(L)):
        if L[i] >= L[p]:
            p = i
    return p

class maClasseA:
    def __init__(self):
        self.x = 0
        self.y = 0

class maClasseB(maClasseA):
    def afficher(self):
        print(self.x,self.y)

obj = maClasseB()
obj.afficher()


ages = [22,10,1]
ages.sort()
print(ages[0])


x = True
y = True
z = True 
print(x and y and z)
print((not x) or (not y) or (not z))
print((not x) and (not y) and (not z))


s = "hbdxca"
if len(s) < 5 or "x" in s:
    print (False)
else:
    print (True)

print(len(s)<5 or "x" in s)
print(not len(s)<5 or "x" in s)
print(len(s)>=5 or "x" not in s)

def monA(n):
    for i in range(n):
        if i % 8 == 0:
            print (i)
            print("A" *i)


a = [10,20,30,40]
b = a[:]
a[1] = 0
print (b)


class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Point('+str(self.x)+','+str(self.y)+')'

def f(x,a,b):
    print(a)
    print(b)
    print(p1)
    a=b
    print(a)
    print(b)
    a.x=1
    a.y=1
    x=x+2
    print(x,a,b)

x=0
p1 = Point(1,2)
p2 = Point(3,4)
f(x,p1,p2)
print (x,p1,p2)


def maFonction1(n):
    res = 1
    for i in range(n):
        res = res * n
    return res

def blabla():
    ages = [22, 19, 23, 10, 34, 31, 20]
    ages.sort()
    print(ages[0])  

x=10
if x < 30:
    print(x, "est inferieur a 30")
elif x > 30:
    print(x, "est superieur a 30")
else:
    print(x, "est 30")



def kiwi(x):
    '''(list)->bool'''
    result=True
    for i in range(len(x)-1):
        if(x[i] > x[i+1]):
            result=False
        else:
            result = True
    return result

m = 1
n = 4
x = m//n

s1 = "bonjour"
s2 = 'tout le monde.'
s = s1 + s2
print(s)

a = 30
print(a%4==0 or a%3==0)

x = [10,2,3]
x[0] = "x"
print(x)

l1 = [11,2,3,7]
l2 = l1
print(l1+l2)


def orange(num):
    t = 0
    for i in range(num):
        t = t + 10
    return t

print("Q21")
class CasNormal:
    def uneMethode(self):
        print("normal")
class CasSpecial:
    def uneMethode(self):
        print("special")
def casQuiConvient(estNormal=True):
    return CasNormal() if estNormal else CasSpecial()

uneInstance = casQuiConvient(estNormal=False)
uneInstance.uneMethode()


print("Q25")
def maFonction25(L):
    X=sorted(L) # sorted(L) retourne une version triée de la liste L
    print(X)
    if len(X)==1:
        print("1")
        return True
    for i in range(len(X)):
        if i==0 and X[i]!=X[i+1]: # X[i] est le premier élément
            print("2 "+ str(i))
            return True
        elif i==len(L)-1 and X[i]!=X[i-1]:# X[i] est le dernier élément
            print("3 "+str(i))
            return True
        elif i!=0 and i!=len(L)-1: # pas le premier ou le dernier
            print("4 "+str(i))
            if X[i]!=X[i-1] and X[i]!=X[i+1]:
                print("5 "+str(i))
                return True
    return False

test1 = maFonction25([1,8,9,7,7])
test2 = maFonction25([2,2,9,7,7])

print("Q20")
def sara(x,y):
    print(x+y)
    return x+y

z = 10 * sara(5,5)
print(z)


print("\"Hello\ni am here\t\"")

str1 = "danny"
str2 = "richard"
str1,str2 = str2,str1
print(str1,str2)

l1 = [1,2,3,4]
l2 = [5,6,7,8]
l1 = l2
l2 = l1
print(l1,l2)


def mask():
    p = 20
    print(p,q)

p,q = 15,38
mask()
print(p,q)

lName='Gebara'
mName='Richard'
def names (lName,fName):
    lName="F"+lName[1:]
    fName='Rick'
    print (lName, mName, fName)
fName='Danny'
names(lName, fName)
print (lName,mName,fName)


lName=['Gebara']
mName=['Richard']
def names (lName,fName):
    lName=['Geb']
    fName=['Rick']
    print (lName, mName, fName)
fName=['Danny']
names(lName, fName)
print (lName,mName,fName)


def ma_fonction(a):
    a[0] = 100
    a[1] = 200

list1 = [1,2,3,4,5]
ma_fonction(list1)
print(list1)


def fifi(ch):
    if len(ch) <= 1:
        return ch
    return fifi(ch[1:]) + 'X'

ch = 'ITI1520'
print(fifi(ch))


class Fany(object):
    num = 0
    
    def compte(self):
        if (Fany.num % 2 != 0):
            print("Fany")
        else:
            print("Oops!")
        Fany.num += 1

b = Fany()
b.compte()
b.compte()
c = Fany()
c.compte()


i = 0
while i < 2:
    j = 0
    while True:
        print("S", end="")
        if j == 2:
            break
        j = j + 1
    print("A", end="")
    i = i + 1


def foo(x):
    global b
    b = b + 1
    for val in x:
        val = val + 10

a = [10, 20, 30]
b = 7
foo(a)
print(a, b)


def foo(a):
    x = [0] * len(a)
    for i in range(len(a)):
        for j in range(len(a[i])):
            x[i] = a[i][j]
    return x

a = [[0, 1], [2, 3], [4, 5]]


def nana(x, y):
    print(x - y)
    return x

n = 2 * nana(10, 10)
print(n)



class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point('+str(self.x)+','+str(self.y)+')'

def foo(x, a):
    a.x = 10
    a.y = 20
    x = x + 2

x = 0
p1 = Point(1, 2)
foo(x, p1)
print(x, p1)

ages = [22,19,23,10,34,31,20]
ages.sort()
print(ages[0])


def ma_fonction77(n):
    for i in range(1,n+1):
        if(n%i == 0):
            print(i, end=" ")
    print()

ma_fonction77(9)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

# Example usage:
num1 = 48
num2 = 18

result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")



class Car:
    def __init__(self, make, model):
        self._make = make  # Using a single leading underscore to indicate it's a protected attribute
        self._model = model
        self._mileage = 0

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_mileage(self):
        return self._mileage

    def drive(self, miles):
        self._mileage += miles


# Creating an instance of the Car class
my_car = Car("Toyota", "Camry")

# Accessing attributes through getter methods
print(f"Make: {my_car.get_make()}")
print(f"Model: {my_car.get_model()}")
print(f"Mileage: {my_car.get_mileage()} miles")

# Driving the car
my_car.drive(100)
print(f"Updated Mileage: {my_car.get_mileage()} miles")



class Point(object):
    def __init__(self, xcoord=0, ycoord=0):
        self.x = xcoord
        self.y = ycoord
    
    def __repr__(self):
        return 'Point('+str(self.x)+','+str(self.y)+')'

def f(x,a,b):
    a=b
    a.x=1000
    a.y=1000
    x=x+3

x=0
p1=Point(1,2)
p2=Point(10,20)
f(x,p1,p2)
print(x, p1, p2)


desserts = [['gateau', 'fromage'], ['creme', 'brulee'], ['chocolat']]
print(desserts[1][1])


def mara(x, y):
    print(x+y)
    return x+y
z = 10 * mara(5,5)
print(z)




class Pointset(object):
       def __init__(self, points):
           self.points = points
points=[Point(1,2), Point(2,1), Point(0,0)]
nouveau_pointset=Pointset(points)
