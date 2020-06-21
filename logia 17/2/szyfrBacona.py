from turtle import *
speed(0)

def kwd(a, k):
    fillcolor(k)
    begin_fill()
    for i in range(4):
        fd(a); lt(90)
    end_fill()

def szyfruj(napis):
    a=min(80, 700/len(napis))
    pu()
    setposition(-a*(len(napis)/2), -2.5*a)
    pd()
    s={
        'A':'aaaaa',
        'B':'aaaab',
        'C':'aaaba',
        'D':'aaabb',
        'E':'aabaa',
        'F':'aabab',
        'G':'aabba',
        'H':'aabbb',
        'I':'abaaa',
        'J':'abaaa',
        'K':'abaab',
        'L':'ababa',
        'M':'ababb',
        'N':'abbaa',
        'O':'abbab',
        'P':'abbba',
        'Q':'abbbb',
        'R':'baaaa',
        'S':'baaab',
        'T':'baaba',
        'U':'baabb',
        'V':'baabb',
        'W':'babaa',
        'X':'babab',
        'Y':'babba',
        'Z':'babbb'}
    
    
    for znak in napis:

        for i in range(5):
            if s[znak][i]=='a':
                kwd(a, "yellow")
            else:
                kwd(a, "blue")
            lt(90)
            fd(a); rt(90)
        rt(90)
        fd(5*a)
        lt(90)
        fd(a)
        




            
