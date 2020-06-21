def natr(tab):
    wyniki = []
    trk = []
    licznik,i = 0,0
    
    while True:
        i+=1
        licznik += i
        trk.append(licznik)
        if licznik >= max(tab):
            break
        
    for liczba in tab:
        
        good = True
        for ltrk in trk:
            if liczba-ltrk in trk:
                wyniki.append([liczba-ltrk,ltrk])
                good = False
                break
            
        if good == True:
            wyniki.append([])
                

    print(wyniki)
                

natr([94,2,3,4,5,30,81])
