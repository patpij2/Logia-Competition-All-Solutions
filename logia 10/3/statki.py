from turtle import *
from random import randint
import numpy as np
speed(0)
tracer(0)

def kwd(kolor):
    begin_fill()
    fillcolor(kolor)
    for i in range(4):
        fd(40); rt(90)
    end_fill()
    


def losuj(n):
    tab = np.zeros((10,10))
    
    if randint(0,1) == 0:
        wiersz = randint(-1,8)
        kolumna = randint(-1,9-n)

        for i in range(3):
            for j in range(n+2):
                if 0<=i+wiersz<=9 and 0<=j+kolumna<=9:
                    tab[i+wiersz][j+kolumna] = 2
                    
        for i in range(n):
            tab[wiersz+1][kolumna+1+i] = 1

    else:
        wiersz = randint(-1,9-n)
        kolumna = randint(-1,8)

        for i in range(n+2):
            for j in range(3):
                if 0<=i+wiersz<=9 and 0<=j+kolumna<=9:
                    tab[i+wiersz][j+kolumna] = 2
                    
        for i in range(n):
            tab[wiersz+1+i][kolumna+1] = 1
        
    return(tab)


def polacz(tab, a):
    wynik = np.zeros((10,10))
    for i in range(10):
        for j in range(10):
            if a[i][j] == 1 or tab[i][j] == 1:
                wynik[i][j] = 1
            elif a[i][j] == 2 or tab[i][j] == 2:
                wynik[i][j] = 2
    return wynik

def jestok(tab, a):
    for i in range(10):
        for j in range(10):
            if a[i][j] == 1 and tab[i][j] == 1:
                return False
            elif a[i][j] == 1 and tab[i][j] == 2:
                return False
            elif a[i][j] == 2 and tab[i][j] == 1:
                return False
    return True
    

def statki():
    pu(); setposition(-200, 200); pd()
    
    tab = np.zeros((10,10))
    a = losuj(4)
    while not jestok(tab,a):
        a = losuj(4)
    tab = polacz(tab, a)

    for i in range(2):
        a = losuj(3)
        while not jestok(tab,a):
            a = losuj(3)
        tab = polacz(tab, a)

    for i in range(3):
        a = losuj(2)
        while not jestok(tab,a):
            a = losuj(2)
        tab = polacz(tab, a)

    for i in range(4):
        a = losuj(1)
        while not jestok(tab,a):
            a = losuj(1)
        tab = polacz(tab, a)

    print(tab)

    for i in range(10):
        for j in range(10):
            if tab[i][j] == 1:
                kwd('green')
            else:
                kwd('white')
            fd(40)
        bk(400)
        rt(90)
        fd(40)
        lt(90)
        
    

statki()
