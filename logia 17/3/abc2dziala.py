def poprawne(slowo):
    for i in range(len(slowo)):
        if (slowo[i] == 'z' or slowo[i] =='c') and ('n' in slowo[i+1:]):
            return False
        
        if slowo[i] == 'z' and ('c' in slowo[i+1:]):
            return False
        
    return True

def szukaj(slowo, i, wyniki):
    print(i)
    if i == 0:
        if poprawne(slowo):
            wyniki.append(slowo)
    else:
        for j in range(len(slowo)):
            szukaj(slowo[0:j]+slowo[j+1:], i-1, wyniki)

def abc(slowo):
    wyniki = []
    i = 0

    while len(wyniki) == 0:
        szukaj(slowo, i, wyniki)
        i+=1
        

    return len(slowo)-len(wyniki[0])

print(
abc('nncnnbffbbbccczzzcz'),
abc('zzzznnnnz') 
)
