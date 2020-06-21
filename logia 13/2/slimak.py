def kiedy(x,y,z):
    dzien=0
    wys=0
    while wys<1000:
        dzien+=1
        wys+=x
        if wys>=1000:
            break
        polka=wys-wys%z
        if wys-y<polka<=wys:
            wys=polka
        else:
            wys-=y
    return dzien
        
        
