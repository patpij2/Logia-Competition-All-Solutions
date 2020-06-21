from turtle import *
speed(0)
tracer(0)

def kwd(a,kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(a); lt(90)
    end_fill()

def litera(l,a):
    l_nr = ord(l) - ord('a')
    licznik = 0

    for j in [5,4,4,3,3,2,2,1,1]:    
        for i in range(j):
            licznik += 1
            if licznik <= l_nr:
                kwd(a,'green')
            else:
                kwd(a,'white') 
            lt(90); fd(a); rt(90)

        fd(a); rt(90)

    fd(3*a); rt(90); fd(3*a); rt(180)
        

def szyfruj(slowo,n):
    poz = 0
    kierunek = 1
    a= min(480/(n*5), 760/(len(slowo)*5))
    
    pu(); setposition(-a*5*(len(slowo)/2),a*5*(n/2)); pd()

    for lit in slowo:
        for i in range(n):
            if i == poz:
                litera(lit,a)
            else:
                kwd(5*a,'white')
        
            pu(); rt(90); fd(5*a); lt(90); pd()
            
        if poz == 0:
            kierunek = 1
        elif poz == n-1:
            kierunek = -1
            
        poz += kierunek
        
        pu(); fd(5*a); lt(90); fd(5*a*n); rt(90); pd()
        
szyfruj("dokumentygoogle",5)    
        
    
