from turtle import *
speed(0)
def trk(a,k):
    fillcolor(k)
    begin_fill()

    fd(a); rt(90); fd(a); rt(135); fd(a*(2**0.5)); rt(135)

    end_fill()

def trk2(a,k):
    fillcolor(k)
    begin_fill()

    fd(a*(2**0.5)); rt(135); fd(a); rt(90); fd(a); rt(135)

    end_fill()


def domki(liczba):
    k = 'white'
    a = min(720/len(str(liczba)), 420/3)
    pu(); setposition(-a*len(str(liczba))+a, 0); pd()
    lt(90)
    for i in str(liczba):
        
        for j in range(8):
            if j+1 == int(i):
                k = 'black'
            else:
                k = 'white'
            
            if j%2 == 0:
                trk(a,k)
            else:
                trk2(a,k)
            rt(45)

        if int(i) == 9:
            k = 'black'
        else:
            k = 'white'

        if int(i) % 2 == 0:
            b = 'gray'
        else:
            b = 'white'
        
        fd(2*a); lt(180); trk(a,b); lt(45); trk2(a,k)

        pu(); fd((2*a)*(2**0.5)); lt(135); pd()
    

domki(912)
