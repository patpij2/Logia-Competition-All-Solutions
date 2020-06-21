from turtle import *
#speed(0)
#tracer(0)

def sk(a):
    pu(); fd(a); pd()

def kwd(a,kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(a); lt(90)
    end_fill()

def domek():
    a = 100
    b = a/5
    pr= 2**0.5

    #ZÓŁTY KWD
    kwd(a,'yellow')

    #OKNA
    sk(b); lt(90); sk(b); rt(90); kwd(b,'blue')
    sk(2*b); kwd(b,'blue');
    sk(-2*b); lt(90); sk(2*b); rt(90); kwd(b, 'blue')
    sk(2*b); kwd(b, 'blue')
    sk(2*b); lt(90); sk(2*b); rt(90)
    
    #DACH
    rt(45)
    fillcolor('red')
    begin_fill()
    fd((2*b)*pr); rt(45); fd(a); rt(135); fd((2*b)*pr); rt(45); fd(a)
    end_fill()
    bk(a); rt(135)

    #SCIANA
    fillcolor('gray')
    begin_fill()
    fd((2*b)*pr); rt(135); fd(a); rt(45); fd((2*b)*pr); rt(135);
    end_fill()


def domki(n):
    if n % 2 == 0:
        pu(); setposition(-1*((n//2 - 1)*60 + (n//2 + 1) * 140 )/2, -90); fd(100); pd()
    else:
        pu(); setposition(-1 *(n//2*60 + (n//2 + 1) * 140 )/2, -90); fd(100); pd()
    
    lt(90)
    a = 100
    b = a/5
    
    domek()
    for i in range(n-1):
        if i % 2 == 0:
            sk(b*2); rt(90); sk(b*7); lt(90); domek()
        else:
            rt(90); sk(b*3); rt(90); sk(b*2); rt(180); domek()
