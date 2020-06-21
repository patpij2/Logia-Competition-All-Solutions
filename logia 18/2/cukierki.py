def ilerazy(n, tab):
    licznik=0
    wynik=0
    wyniki = []
    tab = list(tab)
    
    for i in range(2, len(tab)+2):
        if i%2==0:
            wynik += tab[i-2]
        else:
            wynik -= tab[i-2]

        for n2 in range(wynik+1):
            if n2==n:
                licznik+=1

    
        



    print(licznik)


print(
ilerazy(4, [5, 3, 5, 3, 2, 1]),
ilerazy(2, [3, 2])
)
