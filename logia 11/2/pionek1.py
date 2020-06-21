def pionek(wiersz, pola, cyfra):
    p=pola
    iw=len(pola)/wiersz
    szukana=cyfra
    x,y,ox,oy,mini,lastMini,minx,miny=(0 for i in range(8) )
    tab=[]
    

    for zwiersz in range(len(p)):
        x+=1
        if zwiersz%iw==0:
            x=0
        if zwiersz%iw==0 and zwiersz!=0:
            y+=1
            
        if int(p[zwiersz])==szukana:
            minx=abs(x-ox)
            miny=abs(y-oy)
            lastMini = min(mini, minx+miny, miny, minx)
            tab.append(mini)
            tab.append(minx+miny)
            tab.append(miny)
            tab.append(minx)
            print("ox: ", ox, "  oy: ", oy, "x: ", x, "  y: ", y, "  minx: ", minx, "  miny: ", miny, "  mini: ", mini, " lastMini: ", lastMini)
        
        if int(p[zwiersz])==szukana:
            ox=x
            oy=y   
        print(x,"  ",y, "----", p[zwiersz])

    tab.sort()
    while tab.count(0)>0:
        tab.remove(0)
    print("-------------  ", tab[::])
