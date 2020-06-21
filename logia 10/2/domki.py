from turtle import *
def prk(a):
    for i in range(4):
        fd(a); lt(90)


def domki(n):
    roznica = 0.5/(n-1)
    suma = 0
    domek = 1
    for i in range(n):
        suma += domek
        domek -= roznica
    a = 450/suma

    roznica *= a
    for i in range(n):
        prk(a)
        fd(a)
        print(a)
        a -= roznica
        
domki(5)
