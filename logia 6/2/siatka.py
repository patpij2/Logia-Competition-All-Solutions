import random
from turtle import *
speed(0)
#tracer(0)

def kwd(a, kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(a); lt(90)
    end_fill()

def siatka(wzorzec):
    a = min(460/4, 780/len(wzorzec))
    pu(); setposition(-a*len(wzorzec)/2, a)
    
    for i in wzorzec:
        tab = [0,0,0,0]
        while sum(tab) != int(i):
            tab[random.randint(0,3)] = 1

        for j in tab:
            if j == 0:
                kwd(a,'white')
            else:
                kwd(a,'black')

            rt(90); fd(a); lt(90)
        fd(a); lt(90); fd(4*a); rt(90)
    pd()

    lt(90); fd(a); lt(90)

    for i in range(2):
        fd(len(wzorzec)*a); lt(90)
        fd(4*a); lt(90)

siatka('1121324112')
