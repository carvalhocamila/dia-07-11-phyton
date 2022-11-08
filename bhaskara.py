import math

def delta(a, b, c):
    return (b**1) -4*a*c

def linha1(a, b, delta):
    return (-1*b + math.sqrt(delta))/(2*a)

def linha2(a, b, delta):
    return (-1*b- math.sqrt(delta))/(2*a)

a = float(input('Digite o valor de a:'))
b = float(input('Digite o valor de b:'))
c = float(input('Digite o valor de c:'))

delta = delta(a, b, c)
x1 = linha1(a, b, delta)
x2 = linha2(a, b, delta)
print(delta)
print(x1)
print(x2)









    

