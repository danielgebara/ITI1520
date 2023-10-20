# ITI1520
# Daniel Gebara
# 300401006
# Exercise 2


aha = 'abcdefgh'

result1 = aha[0:4]
print("a) 'abcd':", result1)

result2 = aha[3:6]
print("b) 'def':", result2)

result3 = aha[-1]
print("c) 'h':", result3)

result4 = aha[5:7]
print("d) 'fg':", result4)
    
result5 = aha[3:]
print("e) 'defgh':", result5)

result6 = aha[5:]
print("f) 'fgh':", result6)

result7 = aha[0::2]
print("g) 'adg':", result7)

result8 = aha[1:3] + aha[6]
print("h) 'bd':", result8)