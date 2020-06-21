from turtle import *
import numpy as np
speed(0)

def kwd(a, kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(a)
        rt(90)
    end_fill()

def wzorek(h, s):
    ilew=int(len(s)/h)
    a=min(400/h, 600/ilew)
    pu(); setposition(-(a*(ilew/2)), -(a*(h/2))); pd();
    tab = np.array([int(i) for i in s])
    tab = tab.reshape((ilew, h))

    miejscanaj=[]
    for i in range(ilew):
        miejscanaj.append(sum(tab[i][:]))

    
    lt(90)
    for x in range(ilew):
        for y in range(h):
            if tab[x][y]==0:
                kwd(a, "white")
            elif tab[x][y]==1 and sum(tab[x][:])==max(miejscanaj):
                kwd(a, "red")
            else:
                kwd(a, "gray")
            fd(a)
        bk(a*h)
        rt(90)
        fd(a)
        lt(90)

            
            

    #print(miejscanaj)
    #print(tab)

            


#wzorek(2, '10111001011011')
wzorek(3, '000000000000000000101')
#wzorek(3, '101010111010101010111')
#wzorek(5, '10001011101000101010')  
