def maksos(tab):
    pocz = 0
    kon = 0
    wyniki = []

    for i in range(len(tab)-1):
        if tab[i+1]-tab[i] <= 3:
            kon = i+1
        else:
            wyniki.append(kon-pocz+1)
            pocz = i+1
            kon = i+1

    wyniki.append(kon-pocz+1)

    if tab[0] in [1,2,3]:
        wyniki[0]+=wyniki[-1]
    
    
    print(max(wyniki))


maksos([1,4,7,11,13,14,15,16,27])
maksos([1,4,7,13,14,15,20])
