from turtle import *
speed(0)
#tracer(0)

def kwd(a, k):
    begin_fill()
    fillcolor(k)
    for i in range(4):
        fd(a)
        rt(90)
    end_fill()

def zmieniaczkolorow(s): #Funkcja do zmiany powtarzajacych sie jedynek.
    #Mam problem ze zrobieniem zliczania ich ilosci i kolorowanie tylko tych z najwieksza iloscia powtorzen.
    tab=[int(v) for v in s]
    dozmiany=[]
    licznik=0
    for i in range(len(tab)-1):
        if tab[i]==1:
            if tab[i]==tab[i+1]:
                licznik+=1
                dozmiany.append(i)
                dozmiany.append(i+1)
                dozmiany=list(set(dozmiany))
            dozmiany.sort()
            print(dozmiany)
    for znak in dozmiany:
        tab[znak]=2
    print(dozmiany)
    return tab

def wzorek(h, s):
    a=min(400/h, 600/(len(s)/h))
    pu()
    setposition(-(a*(len(s)/h))/2, -(a*h)/2);
    pd()

    s=zmieniaczkolorow(s)

    lt(90);
    for i in range(len(s)):
        if s[i]==1:
            kwd(a, "gray")
        elif s[i]==0:
            kwd(a, "white")
        elif s[i]==2:
            kwd(a, "red")
        fd(a)
        if (i+1)%h==0:
            bk(a*h)
            rt(90)
            fd(a)
            lt(90)
    
#wzorek(2, '10111001011011')
#wzorek(3, '101010111010101010111')
wzorek(5, '10001011101000101010')
