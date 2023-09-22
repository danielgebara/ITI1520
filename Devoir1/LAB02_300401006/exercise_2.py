# ITI1520
# Daniel Gebara
# 300401006
# Exercise 2

def celcius_en_fahrenheit(temp_Celcius):
    ''' (float,float) -> float '''
# transforme la temperature de celcius en fahrenheit 
    temp_Fahrenheit = 9.0 / 5.0 * temp_Celcius + 32
    return temp_Fahrenheit

t_celcius = 30
t_fahrenheit = celcius_en_fahrenheit(t_celcius)
print (t_celcius, "Celcius est", t_fahrenheit, "Fahrenheit.")