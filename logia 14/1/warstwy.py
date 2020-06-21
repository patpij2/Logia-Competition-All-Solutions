from turtle import *
speed(0)

def kwadrat(dl):
    for i in range(4):
        fd(dl); lt(90)

def poziomy(a,b):
    for i in range(a):
        kwadrat(b/a); fd(b/a)
    lt(180); fd(b)
    rt(90); fd(b/a)
    rt(90)

def zliczanie(a,b):
    zliczanko=0
    for i in range(a):
        zliczanko+=b/a
    return zliczanko

def warstwy(c, d):
    pu()
    setposition(-(d/2),-(zliczanie(c,d))); pd()
    for i in range(1,c+1):
        poziomy(i,d)
