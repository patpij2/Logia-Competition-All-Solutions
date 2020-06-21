def ms(n, zabud):
    tab = [[0 for i in range(n+2)] for j in range(n+2)]
    wyniki, domy_wyniki = [], []
    liczba, maks = 0, -1000000
    
    for w in range(1, n+1): #DODAWANIE DO 2-WYMIAROWEJ TABLCY 1 W MIEJSCA ZABUDOWANYCH DOMÓW
        for k in range(1, n+1):
            if n*(w-1)+k in zabud:
                tab[w][k] = 1

    for w in range(1, n+1): #SZUKANIE DOMOW BEZ ZABUDOWY I ZLICZANIE
        for k in range(1, n+1):
            if tab[w][k] != 1:
                wynik = tab[w+1][k] + tab[w-1][k] + tab[w][k+1] + tab[w][k-1]
                liczba = n*(w-1)+k
                wyniki.append([liczba,wynik]) #DODAWANIE DO TABLICY WYNIKI SUMY I OBLICZONEJ POZYCJI LICZBY

    for maksdom in wyniki: #WYZNACZANIE MAKSA Z TABLICY WYNIKI
        maks = max(maks, maksdom[1])

    for dom in wyniki: #DODAWANIE TYCH DOMOW DO OSTATECZNYCH WYNIKOW KTORE == MAKS
        if dom[1] == maks:
            domy_wyniki.append(dom[0])
    
    return domy_wyniki

print(
ms(4,[9,10,14]),
ms(3,[4,5,6]),
ms(5,[1,7,13,19,25])
)
