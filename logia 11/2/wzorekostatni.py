from turtle import *
import numpy as np
speed(0)

def kwd(a, k):
    begin_fill()
    fillcolor(k)
    for i in range(4):
        fd(a)
        rt(90)
    end_fill()

def wzorek(h, s):
    a=min(400/h, 600/(len(s)/h))
    pu()
    setposition(-(a*(len(s)/h))/2, -(a*h)/2);
    pd()
    ilew=int(len(s)/h)
    tab = np.array( [int(i) for i in s] )
    tab = tab.reshape((ilew, h))

    rozmiary = []
    lt(90)
    
    for i in range(ilew):
        rozmiary.append(sum(tab[i][:]))
    maksimum = max(rozmiary)

    for x in range(ilew):
        for y in range(h):
            if tab[x][y]==0:
                kwd(a, "white")
            elif tab[x][y]==1 and sum(tab[x][:])==maksimum:
                kwd(a, "red")
            else:
                kwd(a, "gray")
            fd(a)
        bk(a*h)
        rt(90)
        fd(a)
        lt(90)

wzorek(2, '10111001011011')
#wzorek(3, '101010111010101010111')
#wzorek(5, '10001011101000101010')   
        
