from turtle import *
import numpy as np
speed(0)

def rysuj(a, liczba):
    b = a
    for i in range(liczba):
        fd(b)
        lt(90)
        b-=4
        
        
        

def dekoduj(litera, tab):
    for x in range(5):
        for y in range(6):
            if tab[y][x] == litera:
                return x+y
    if litera == 'j':
        return 5
    
    
def koduj(napis):
    a = 780/ (len(napis) + (len(napis)-1) * 0.2)
    
    alfabet = '00000abcdefghiklmnopqrstuvwxyz'
    tab = np.array([v for v in alfabet])
    tab = tab.reshape((6,5))

    for i in range(len(napis)):
        setheading(0)
        pu(); setposition(-390+(1.2*a*i), 0); pd()
        liczba = dekoduj(napis[i], tab)
        rysuj(a, liczba)
        
    


koduj("pa")
