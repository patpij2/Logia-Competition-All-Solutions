def czyrowna(a):
    suma=0
    iloczyn=1
    b=str(a)
    if len(b)==1:
        return True
    else:
        for v in range(len(b)):
            suma+=int(b[v])
            iloczyn*=int(b[v])
            
    if suma == iloczyn:
        return True
    else:
        return False

def irs(n):
    licznik=0
    ktora=0
    while n>licznik:
        ktora+=1
        if czyrowna(ktora)==True:
            licznik+=1
            ostatnia=ktora
            print(ktora)
    return(ktora)
            
        
    
