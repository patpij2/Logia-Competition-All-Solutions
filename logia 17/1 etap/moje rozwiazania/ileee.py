def ile(strony):
    licznik=0
    for i in range(strony):
        stronastr=str(i)
        dlugosc=len(str(i))
        
        if i<12:
            continue

        for n in range(dlugosc-1):
            if int(stronastr[n] + stronastr[n+1])==13:
                licznik+=2

    print(licznik)
        
        
