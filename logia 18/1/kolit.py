def kolit(napis):
    licznik=0
    b= [i for i in napis]
    while len(b)>0:
        i=0
        krok=1
        good=True
        litera=b[0]
        while i<len(b):     # zliczajacy
            if litera != b[i]: #szukamy bledu
                good=False
                
            b[i]='0' #zamieniamy na 0
            i+=krok # co 1,2,3... tworzy piramidke
            krok+=1
        if good:
            licznik+=1
        for i in range(len(b)-1, -1, -1): # kasowanie 0
            print(b[i])
            if b[i]=='0':
                del(b[i])
    return licznik
            
    
        
        
    
#numpy sprawdz
