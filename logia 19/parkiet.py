from turtle import *
#speed(0)
#tracer(0)

def sk(a):
    pu(); fd(a); pd()

def kwd(a=30,k = 'green'):
    fillcolor(k)
    begin_fill()
    for i in range(4):
        fd(a); rt(90)
    end_fill()

def trk(a=30):
    fillcolor('yellow')
    begin_fill()
    for i in range(3):
        rt(120); fd(a)
    end_fill()

def sym1(a=30):
    lt(180); bk(a*2); lt(90);
    kwd(); rt(180); trk(); bk(a); rt(90); trk(); bk(a); trk(); lt(180); kwd()
    lt(120); fd(a); lt(120); kwd(k='blue')
    lt(60); fd(a); lt(60); fd(a); rt(90); fd(a); lt(270)
    
def sym2(a=30):
    kwd(); rt(180); trk(); bk(a); rt(180); kwd(); rt(180); trk(); bk(a)
    rt(60); kwd(k='blue'); rt(30); trk(); lt(90); fd(2*a); lt(180)
    
def kafelka():
    a=30
    sk(a/2); lt(90); sym1()
    lt(90); sk(a/2); rt(90); sk(a*3+a*((3**0.5)/2)); rt(90); sym2()
    rt(90); sk(a*3+a*((3**0.5)/2)); lt(90); sk(1.5*a+a*(3**0.5)/2); lt(90); sk(1.5*a)
    rt(90); sym2()
    lt(60); sk(a); lt(30); sym1()
    lt(150); sk(a); rt(30); sk(a); lt(60); sk(a); rt(90); sk(1.5*a); rt(180)
    
def parkiet():
    a=30
    pu(); setposition(-1.5*(a*3+(a*((3**0.5)/2)*2)), 0.5*(a*3+(a*((3**0.5)/2)*2))); pd()
    
    for j in range(3):
        kafelka()
        for i in range(2):
            rt(90); sk(a*3+(a*((3**0.5)/2)*2)); lt(90); kafelka()
            
        sk(a*3+(a*((3**0.5)/2)*2)); lt(90); sk((a*3+(a*((3**0.5)/2)*2))*2); rt(90)
