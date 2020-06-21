def dzielniki(a,b):
    ile = 0
    wyniki = []
    
    for i in range(a,b):
        licznik = 0
        if int(i**0.5)**2 == i:  
            for j in range(i):
                if i!=0 and j!=0 and i%j == 0:
                    licznik+=1
            if licznik == 2:
                ile+=1

    print(ile)
    
dzielniki(2, 6)
dzielniki(80000,90000)
