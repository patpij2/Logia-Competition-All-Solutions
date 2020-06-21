def pionek(wiersz, pola, cyfra):
    p=pola
    x=0
    y=0
    ox=0
    oy=0
    iw=len(pola)/wiersz
    mini=0
    akmini=0
    minx=0
    miny=0
    szukana=cyfra

    for zwiersz in range(len(p)):
        print(x,"  ",y, "----", p[zwiersz]) 
        x+=1
        if zwiersz%iw==0:
            x=0
            #print(x,"  ",y)
        if zwiersz%iw==0 and zwiersz!=0:
            y+=1
