def czyPierwsza(n):
    licznik = 0
    for i in range(1, n+1):
        if n%i == 0:
            licznik+=1
    if licznik == 2:
        return True
    return False

def lllp(n):
    wyniki = []
    i=100
    while len(wyniki) < n:
        if czyPierwsza(i):
            j = int(str(i)[::-1])
            if czyPierwsza(j) and i!=j:
                wyniki.append(int(str(i)+str(j)))
        i+=1

    return wyniki

print(
lllp(0),
lllp(2),
lllp(10)
)
####
            
