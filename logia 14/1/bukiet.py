from turtle import *
speed(0)

def trap(a,b):
    begin_fill()
    fillcolor(b)
    fd(a);
    rt(45)
    fd(a)
    rt(135)
    fd(a);
    rt(45)
    fd(a)
    rt(135)
    end_fill()

def gwiazdka(a):
    for i in range(8):
        lt(45)
        if i%2==0:
            trap(a, "yellow")
        else:
            trap(a, "blue")

def odnozek(a):
    gwiazdka(a)
    lt(90)
    fd(60+2*a)
    gwiazdka(a)
    rt(135)
    fd(60+2*a)
    rt(45)
    gwiazdka(a)
    fd(60+2*a)
    gwiazdka(a)
    fd(60+2*a)
    bk(60+2*a)
    rt(45)
    fd(60+2*a)
    bk(60+2*a)
    rt(90)
    fd(60+2*a)
    rt(135)
    
def BUKIET():
    gwiazdka(60)
    b=75
    for i in range(8):
        rt(45)
        
        fd(b);
        rt(45)
        fd(b)

        lt(45)
        odnozek(15)
        rt(45)
        
        rt(135)
        fd(b);
        rt(45)
        fd(b)
        rt(135)

    
