import numpy as np
from turtle import *
speed(0)

def rysuj(a, litera):
    b = a
    
    for i in range(litera):
        fd(b)
        lt(90)
        b-=4
    
    

def koduj(napis):
    a = 780 / len(napis)+(len(napis)-1) * 0.2
    pu(); setposition(-340, 0); pd()

    c = 0
    
    alfabet = '00000abcdefghiklmnopqrstuvwxyz'
    tab = np.array([i for i in alfabet])
    tab = tab.reshape((6,5))

    for l in range(len(napis)):
        if napis[l]=='j':
            c='i'
        else:
            c= napis[l]
        for i in range(5):
            for j in range(6):
                if tab[j][i] == c:
                    setheading(0)
                    pu(); setposition(-390, 0)
                    fd(a*(1.2*l)); pd()
                    rysuj(a, i+j)

koduj("wlodek")
