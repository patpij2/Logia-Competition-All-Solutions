from turtle import *
speed(0)
#tracer(0)

def trk(a,k):
    fillcolor(k)
    begin_fill()

    for i in range(3):
        fd(a); rt(120)

    end_fill()

    
def rysuj(a,l):
    if l == 8:
        trk(a,'black')
    else:
        trk(a,'white')

    lt(60)

    if l == 2:
        trk(a,'black')
    else:
        trk(a,'white')

    rt(120)
    
    if l == 1:
        trk(a,'black')
    else:
        trk(a,'white')

    lt(60); fd(a); rt(60)

    if l == 4:
        trk(a,'black')
    else:
        trk(a,'white')
    
    lt(60);
    #pu(); fd(a); pd(); rt(180)
    
def kodsum(l):
    moneta = 8
    li = l
    i = 0
    while li > 0:
        if li >= moneta:
            i+=1
            li -= moneta
        else:
            moneta //= 2
            
    moneta = 8
    a = min(360/i*2, 420/(3**0.5))
    pu(); setposition(-a*(i/2), 0); pd()
    
    i = 0
    while l > 0:
        i +=1
        if l >= moneta:
            rysuj(a,moneta)
            if i %2 ==1:
                pu(); fd(a); pd(); rt(180)
            else:
                pu(); bk(a); pd(); rt(180)
                
            l -= moneta
        else:
            moneta //= 2

kodsum(101)
