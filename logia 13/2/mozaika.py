from turtle import *
speed(0)

def kwd(a, kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(a)
        rt(90)
    end_fill()

def rysuj(a, wiersz):
    for znak in wiersz:
        if znak == "c":
            kwd(a, "red")
        elif znak == "z":
            kwd(a, "green"). 
        elif znak == "x":
            kwd(a, "black")
        elif znak == "b":
            kwd(a, "white")
        elif znak == "f":
            kwd(a, "purple")
        rt(90)
        fd(a)
        lt(90)
    

def szyfruj(kolory, klucz):
    p=klucz%len(kolory)
    tmp=kolory
    for i in range(p):
        '''nowa=[tmp[-1]]
        nowa.extend(tmp[:-1])'''
        nowa=[]
        nowa.extend(tmp[1:])
        nowa.append(tmp[0])
        tmp=nowa
    return tmp
    

def koduj(kolory, nowekolory, wiersz):
    wynik=""
    for znak in wiersz:
        i=kolory.index(znak)
        wynik+=nowekolory[i]
    return wynik


def mozaika(kolory, klucz, wiersz):
    pu()
    a=min(300/(len(kolory)+1), 600/len(wiersz)); 
    setposition(-1*(a*len(wiersz))/2, -1*(a*len(kolory)+1)/2); pd()
    lt(90)
    rysuj(a, wiersz)
    lt(90)
    fd(a*len(wiersz))
    rt(90)
    fd(a)

    for i in range(len(kolory)):
        nowekolory=szyfruj(kolory, klucz);
        wiersz=koduj(kolory, nowekolory, wiersz)
        rysuj(a, wiersz)
        lt(90)
        fd(a*len(wiersz))
        rt(90)
        fd(a)


        
