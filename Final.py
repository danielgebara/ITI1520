def maFonction(L):
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
y = False
z = False 
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
    a=b
    a.x=1
    a.y=1
    x=x+2

x=0
p1 = Point(1,2)
p2 = Point(3,4)
f(x,p1,p2)
print (x,p1,p2)



def maFonction(n):
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