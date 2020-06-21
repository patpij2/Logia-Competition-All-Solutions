from turtle import *
speed(0)
def trk():
    a = 80
    fillcolor('white')
    begin_fill()
    for i in range(3):
        fd(a); lt(360/3)
    end_fill()

def kat6(k):
    a=40
    for i in range(6):
        fd(a); trk(); lt(360/6)

    fillcolor(k)
    begin_fill()
    for i in range(6):
        fd(a); lt(360/6)
        
    end_fill()
    
def kwiat3(ktab):
    kat6(ktab[0]);
    pu(); lt(60); fd(40); rt(60); fd(80); pd()
    kat6(ktab[1])
    pu(); rt(120); fd(40); lt(120); rt(120);
    pd(); kat6(ktab[2])

    pu();lt(120); fd(80); rt(60); fd(40); lt(60); pd()

def ko(n):
    if n == 0:
        return 'red'
    elif n == 1:
        return 'yellow'
    else:
        return 'blue'

def sze(l):
    rt(30)
    l = str(l)
    kwiat3( [ ko( l.count('0')), ko( l.count('1')), ko( l.count('2')) ] )
    kwiat3( [ ko( l.count('3')), ko( l.count('4')), ko( l.count('5')) ] )
    kwiat3( [ ko( l.count('6')), ko( l.count('7')), ko( l.count('8')) ] )
    kat6( ko( l.count('9')) )
    
sze(321458973)
