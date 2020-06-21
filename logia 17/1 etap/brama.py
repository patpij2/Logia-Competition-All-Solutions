from turtle import *
speed(0)


def prk(a, b):
    begin_fill()
    for i in range(2):
        fd(a)
        lt(90)
        fd(b)
        lt(90)
    end_fill()
	
def slupek(a):
    fillcolor("red")
    begin_fill()
    for i in range(2): #prostokat dolny
        fd(a)
        lt(90)
        fd(a*5)
        lt(90)
    end_fill()

    lt(90) #prostokat wyzej
    fd(a*5)
    rt(90)
    fd(2*a)
    lt(90)

    begin_fill()
    for i in range(2): #prostokat dolny
        fd(a)
        lt(90)
        fd(a*3)
        lt(90)
    end_fill()

    begin_fill() #trojkat
    fd(a)
    rt(90)
    fd(a)
    lt(135)
    fd((a*2.5)*2**(0.5))
    lt(135-45)
    fd((a*2.5)*2**(0.5))
    lt(135)
    fd(4*a)
    end_fill()

    pu()
    rt(90)
    fd(a*6)
    rt(90)
    fd(2*a)
    rt(90)
    pd()


def furtka(a):
    rt(90) #pozycja
    fd(4*a)
    
    fillcolor("red") #czerwony prostokat lewy
    begin_fill()
    lt(90)
    fd(12*a)
    rt(90)
    fd(2*a)
    rt(90)
    fd(12*a)
    rt(90)
    fd(2*a)
    end_fill()

    rt(180) #pozycja
    fd(a*16)
    
    fillcolor("red") #czerwony prostokat prawy
    begin_fill()
    lt(90)
    fd(12*a)
    rt(90)
    fd(2*a)
    rt(90)
    fd(12*a)
    rt(90)
    fd(2*a)
    end_fill()

    fd(a*16) #pozycja
    rt(90)
    fd(a*12)
    lt(90)
    fd(a*5)

    begin_fill() #trapez
    rt(135)
    fd(a*2**(0.5))
    rt(45)
    fd(a*26)
    rt(45)
    fd(a*2**(0.5))
    rt(135)
    fd(a*23)
    end_fill()

    rt(90)
    pu()
    fd(a)
    pd()

    prk(a, a) #kwadraty
    rt(90)
    fd(2*a)
    lt(90)
    prk(2*a, 2*a)
    rt(90)
    fd(a)
    lt(90)
    prk(a, a)

    rt(90)	#pozycja
    fd((26-13)*a)
    lt(90)
    
    prk(a, a)	#kwadraty
    rt(90)
    fd(2*a)
    lt(90)
    prk(2*a, 2*a)
    rt(90)
    fd(a)
    lt(90)
    prk(a, a)

    pu()
    rt(90)
    fd(3*a)
    lt(90)
    fd(2*a)
    pd()

    begin_fill()
    rt(45)
    fd((a*2)*2**(0.5))
    lt(135)
    fd(a*30)
    lt(135)
    fd((a*2)*2**(0.5))
    lt(45)
    fd(a*26)
    
    end_fill()

    pu()
    lt(90)
    fd(2*a)
    rt(90)
    pd()

    begin_fill()
    fd(3*a)
    lt(135)
    fd(a*2**(0.5))
    lt(45)
    fd(a*30)
    lt(45)
    fd(a*2**(0.5))
    lt(135)
    fd(a*32)
    end_fill()
    
def brama():
    pu() #pozycja
    setposition(-312, -228)
    pd()

    fillcolor("gray") #szary prostokat
    begin_fill()
    fd(624); rt(90)
    fd(24); rt(90)
    fd(624); rt(90)
    fd(24); rt(90)
    end_fill()
    
    
    fd(24); #rozmiecznenie daszkow
    slupek(24)
    rt(90)
    fd(24*7)
    slupek(24)
    rt(90)
    fd(24*9)
    slupek(24)
    rt(90)
    fd(24*7)
    slupek(24)

    lt(90) #powrot
    fd(24*24)
    rt(90)

    furtka(24)
    pu()
    setposition(-312, -228)
    pd()
    
brama()
done()
