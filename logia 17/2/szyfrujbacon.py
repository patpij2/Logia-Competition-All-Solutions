def szyfruj():
    klucze = []
    for i in range(0,24):
        a = bin(i)[2:].rjust(5,'0')
        a = a.replace('0','a')
        a = a.replace('1','b')
        klucze.append(a)

    klucze.insert(9,'abaaa')
    klucze.insert(21,'baabb')

    alfa = [ chr(i).capitalize() for i in range(97,97+26)]
    slownik = {alfa[i]:klucze[i] for i in range(len(alfa))}
    
    
    print(slownik)
            
szyfruj()
