from turtle import *
speed(0)
tracer(0)

def znaczek(a):
    #znaczek dolny 1
    begin_fill()
    fd(a*8)
    lt(90)
    fd(a*2)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    rt(90)
    fd(a*7)
    lt(90)
    fd(a)
    end_fill()

    #znaczek boczny
    lt(90)
    pu()
    fd(a*10)
    lt(90)
    pd()
    begin_fill()
    fd(a*4)
    lt(90)
    fd(a)
    lt(90)
    fd(a*3)
    lt(45)
    fd(a*2**(0.5))
    end_fill()

    #znaczek górny
    lt(135)
    pu()
    fd(a*5)
    lt(45)
    pd()
    begin_fill()
    fd(a*2**(0.5))
    lt(45)
    fd(a*7)
    lt(90)
    fd(a*2)
    lt(45)
    fd(a*2**(0.5))
    lt(135)
    fd(a*2)
    rt(90)
    fd(a*7)
    end_fill()

    #znaczek srodkowy
    lt(180)
    pu()
    fd(a*6)
    lt(90)
    fd(a)
    pd()
    begin_fill()
    fd(a)
    lt(90)
    fd(a*4)
    lt(135)
    fd(a*2**(0.5))
    lt(45)
    fd(a*3)
    end_fill()

    #powrot

    lt(180)
    pu()
    fd(a*6)
    rt(90)
    fd(a*4)
    lt(90)
    pd()
    

def pasek(a):
    pu()
    fd(a)
    pd()
    begin_fill()
    fd(a*7)
    lt(90)
    fd(a)
    lt(90)
    fd(a*7)
    lt(90)
    fd(a)
    end_fill()
    
    lt(90)
    fd(a*7)
    lt(90)
    fd(a)

def rama(n):
    pu()
    setposition(-240, -240)
    pd()
    
    a=480/(n*10+8)

    for j in range(4):
        for i in range(n):
            znaczek(a)

        pasek(a)
    
    

