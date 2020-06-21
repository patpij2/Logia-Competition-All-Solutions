def poler(napis):
    gora, dol, prawo, lewo, x, y = (0 for i in range(6))
    #w numpy np.zeros(6)
    for znak in napis:
        if znak=='g':
            y+=1
            
        elif znak=='d':
            y-=1

        elif znak=='p':
            x+=1

        elif znak=='l':
            x-=1

        prawo=max(x, prawo)
        lewo=min(x, lewo)
        gora=max(y, gora)
        dol=min(y, dol)

    return (prawo-lewo)*(gora-dol)
            
