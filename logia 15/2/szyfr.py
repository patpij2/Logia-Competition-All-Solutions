from turtle import *
speed(0)

def prostokat(a,b):
    fd(a); rt(90)
    fd(b); rt(90)
    fd(a); rt(90)
    fd(b); rt(90)
    fd(a)
    

def szyfr(alfabet, slowo):
    licznik = 0
    for i in range(len(slowo)):
        licznik += i*10+10
    
    pu(); setposition(-licznik/2, 0); pd()
    samo = ['a','e','i','o','u','y']
    
    for i in range(len(slowo)):
        szer=10*i+10
        wys= alfabet.index(slowo[i])*10+10
        
        if slowo[i] in samo:
            prostokat(szer,wys)
        else:
            prostokat(szer,-wys)
        
#szyfr('abcdefghijklmno','lajkonik')
szyfr('rklot','otok')
