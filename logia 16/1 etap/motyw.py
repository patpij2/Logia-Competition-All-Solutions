from turtle import *
speed(0)
tracer(0)

def trk():
    a=480/15
    fillcolor("black")
    begin_fill()
    lt(45)
    fd((a/2)*2**(0.5))
    rt(90)
    fd((a/2)*2**(0.5))
    rt(135)
    fd(a)
    end_fill()
    rt(180)

def liniatrk(ilosc):
    a=480/15
    for j in range(ilosc):
        trk()
        fd(a)
    
def kafelka1():
    a=480/15
    for i in range(4): # kafelka zew
        liniatrk(5)
        lt(90)

    pu() #pozycja
    fd(a)
    lt(90)
    fd(a)
    rt(90)
    pd()


    for v in range(4): #kafelka wew
        liniatrk(3)
        lt(90)


    pu() #pozcyja
    fd(a)
    lt(90)
    fd(a)
    rt(90)
    pd()

    begin_fill()
    for v in range(4): #kafelka najwew
        fd(a)
        lt(90)
    end_fill()

    pu() #pozycja
    rt(90)
    fd(2*a)
    lt(90)
    fd(3*a)
    pd()

#------------kafelka2
def kafelka2():
    a=480/15
    
    for k in range(4):
        fd(5*a)
        lt(90)
    
    pu() #pozycja
    fd(a)
    lt(90)
    fd(a)
    rt(90)
    pd()


    for v in range(4): #kafelka wew
        liniatrk(3)
        lt(90)


    pu() #pozcyja
    fd(a)
    lt(90)
    fd(a)
    rt(90)
    pd()

    begin_fill()
    for v in range(4): #kafelka najwew
        fd(a)
        lt(90)
    end_fill()

    pu() #pozycja
    rt(90)
    fd(2*a)
    lt(90)
    fd(3*a)
    pd()
    


def motyw():
    a=480/15
    '''pu()
    setposition(-240, -240)
    pd()

    kafelka1()
    kafelka2()
    kafelka1()


#-----------------

    pu()
    setposition(-240, (240-(5*a)))
    pd()

    kafelka1()
    kafelka2()
    kafelka1()


#-----------------

    pu()
    setposition(-240, (240-(10*a)))
    pd()

    kafelka2()
    kafelka1()
    kafelka2()
'''
    for i in range(3):
        pu()
        setposition(-240, -240+(5*a*i) )
        pd()
        for j in range(3):
            
            if (i+j)%2==0:
                kafelka1()
            else:
                kafelka2()
                
            
    
    
