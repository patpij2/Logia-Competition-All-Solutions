from turtle import *
def kwd(a,nr):
    for i in range(4):
        fd(a); lt(90)
        
    write(str(nr))
    
    fd(a)

def rysuj(gra):
    a=50
    for i in gra:
        kwd(a,i[0])
        kwd(a,i[1])
    
    

def domino(gra):
    gra_nor = [[gra[i],gra[i+1]] for i in range(len(gra)-1)]
    gra_spr = [[gra[i],gra[i+1]] for i in range(len(gra)-1)]

    for i in range(len(gra_spr)):
        gra_spr[i].sort()

    for i in range(len(gra_spr)):
        if gra_spr.count(gra_spr[i]) != 1:
            return 'blad'

    rysuj(gra_nor)

print(
domino('1032')
)
