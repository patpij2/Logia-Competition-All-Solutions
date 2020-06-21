def redukcja(liczba):
    tab = [int(i) for i in str(liczba)]
    good = True
    licznik = 1

    while licznik != 0:
        licznik = 0
        print(tab)
        for j in range(len(tab)-1):
            if tab[j]==tab[j+1]:
                licznik+=1
                tab[j] = 0
                tab[j+1]=int(str(tab[j+1]*2)[-1])

        tab = [i for i in tab if i!=0]
        
    tab = [str(i) for i in tab]
    
    return ''.join(tab)

print(
redukcja(426633),
redukcja(84211)
)
