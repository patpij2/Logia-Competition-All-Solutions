from turtle import *
def galaz(kod,dl):
    fd(dl)
    if len(kod) >= 1:
        lt(45); fd(2/3* dl)
        galaz(kod[0],2/3*dl)
        bk(2/3*dl); rt(45)
    if len(kod) == 2:
        rt(45); fd(2/3*dl)
        galaz(kod[1],2/3*dl)
        bk(2/3*dl); lt(45)
    
    bk(dl)
galaz([[[[],[]],[[],[]]],[]],100)
