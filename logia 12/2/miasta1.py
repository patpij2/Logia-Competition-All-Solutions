from itertools import permutations
from random import randint

def porownaj(p,a):
    minimum = 10000000
    for i in range(10000):
        c,d = a,p
        licznik = 0
        while c != d:
            licznik+=1
            j = randint(0,len(a)-2)
            k = j+1
            tmp = c[j]
            tmp2 = c[k]
            c = c[0:k] + tmp + c[k+1:]
            c = c[0:j] + tmp2 + c[j+1:]
            #c = c[0:j] + tmp2 + tmp + c[k+1:]
        minimum = min(licznik, minimum)
    return(minimum)
    

def miasta(a,t,z):
    minimum = 1000000000
    for p in list(permutations(a)):
        ocena = 0
        napis = ''.join(p)
        ocena = ocena + porownaj(napis,a)
        ocena = ocena + porownaj(napis,t)
        ocena = ocena + porownaj(napis,z)

        if ocena < minimum:
            minimum = ocena
            wynik = p

    print(wynik)

miasta("PŁKW", "WPŁK", "PWKŁ")
