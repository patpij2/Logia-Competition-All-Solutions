from turtle import *
import random
speed(0)
def kwd(a):
    tab = ['green','blue','tomato','olive','red','yellow']
    fillcolor(random.choice(tab))
    begin_fill()
    for i in range(4):
        fd(a); lt(90)
    end_fill()
    
def kwadraty(x,y):
    #fd(x); lt(90); fd(y); lt(90); fd(x); lt(90); fd(y); lt(90)

    while x> 0 and y>0:
        if x > y:
            kwd(y); fd(y)
            x-=y
        else:
            kwd(x); lt(90); fd(x); rt(90)
            y-=x

def kwadreku(x,y):
    #fd(x); lt(90); fd(y); lt(90); fd(x); lt(90); fd(y); lt(90)

    if x> 0 and y>0:
        if x > y:
            kwd(y); fd(y)
            kwadreku(x-y,y)
        else:
            kwd(x); lt(90); fd(x); rt(90)
            kwadreku(x,y-x)
        
    
kwadreku(163,255)
