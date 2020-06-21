def odl(i,j,n):
    odleglosc1x = abs(i[0] - j[0])
    odleglosc2x = abs(n-odleglosc1x)
    
    odleglosc1y = abs(i[1] - j[1])
    odleglosc2y = abs(n-odleglosc1y)
    
    return min(odleglosc1x,odleglosc2x) + min(odleglosc1y,odleglosc2y)

def planeta(n,domy):
    tab = [0 for i in range(len(domy))]
    licznik = 1

    for i in domy:
        for j in domy:
            if i != j and odl(i,j,n) <= 5:
                if  tab[domy.index(i)] != 0 and tab[domy.index(j)] == 0:
                    tab[domy.index(j)] = tab[domy.index(i)]

                elif tab[domy.index(j)] != 0 and tab[domy.index(i)] == 0:
                    tab[domy.index(i)] = tab[domy.index(j)]

                elif tab[domy.index(j)] == 0 and tab[domy.index(i)] == 0:
                    tab[domy.index(i)] = licznik
                    licznik +=1
                    #print(licznik)
    maksimum = 0
    for i in range(1,licznik+1):
        maksimum = max(maksimum, tab.count(i))

    return maksimum

print(
planeta(12,[[3,1],[1,1],[1,3],[2,12],[9,5],[8,6]]),
planeta(100,[[6,6],[6,11],[11,6],[11,11],[80,80]])
)
