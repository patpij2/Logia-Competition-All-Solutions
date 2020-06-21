def ile(n):
    moneta=3**12
    ilosc=0

    while n>0:
        if moneta<=n:
            ilosc+=(n- n%moneta)/moneta
            n = n % moneta 
        else:
            moneta=moneta/3
            
    return int(ilosc)
    
