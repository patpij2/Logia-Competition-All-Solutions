def warunek(a):
    suma=0
    iloczyn=1
    for znak in a:
        suma+=int(znak)
        iloczyn*=int(znak)
        
    if suma==iloczyn:
        return True
    else:
        return False
        

def irs(n):
    licznik=0
    i=0
    while licznik<n:
        i+=1
        if warunek(str(i)):
            licznik+=1
    return i
