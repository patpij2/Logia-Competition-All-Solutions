from turtle import *
speed(0)

def skok(a,b):
    x,y = position()
    setposition(x+a,y+b)

def rys(n,a):
    x,y = position()
    
    if n!=9:
        skok(a,a)
        pu(); skok(-a, 0); pd()
        skok(a,-a)

        if n>=1:
            pu(); skok(-a,0); pd()
            skok(0,a)

        if n>=2:
            pu(); skok(a,-a); pd()
            skok(0,a)

        if n>=3:
            pu(); skok(-(a/2),-a); pd()
            skok(0,a)

        if n>=4:
            pu(); skok(-(a/2),-a); pd()
            skok(a,0)

        if n>=5:
            pu(); skok(0,a); pd()
            skok(-a,0)

        if n>=6:
            pu(); skok(0,-(a/2)); pd()
            skok(a,0)

        if n>=7:
            pu(); skok(-((3/4)*a),-(a/2)); pd()
            skok(0,a)

        if n>=8:
            pu(); skok((1/2)*a,0), pd()
            skok(0,-a)

    if n==9:
        skok(a/2,0); skok(0,a); skok(-(a/2), 0); skok(0, -a)
        pu(); setposition(x+(a/2),y); pd()
            
    if n!=9:        
        pu(); setposition(x+a,y); pd()

def ol(s):
    s = str(s)
    liczb9 = s.count('9')
    a = 720/((len(s)*1.5)-0.5-liczb9*0.5)
    pu(); setposition(-720/2,-a/2); pd()
    
    for i in s:
        rys(int(i),a)
        pu(); fd(a/2); pd()
    


ol(59432434291459)
