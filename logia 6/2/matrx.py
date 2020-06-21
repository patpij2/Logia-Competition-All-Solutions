from turtle import *
speed(0)

def kat6(a):
    begin_fill()
    for i in range(6):
        fd(a); lt(60)
    end_fill()

def matrx(x):
    a=10
    
    trk = 1
    i = 1
    
    while trk <= x:
        i+=1
        trk += i
    trk -=i

    pu()
    for j in range(1,i):
        for k in range(j):
            kat6(a); fd(3*a)
        bk(3*a*j); rt(120); fd(3*a); lt(120)

        
        

        
    pd()
matrx(45)
