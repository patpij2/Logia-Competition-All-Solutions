def redukcja(liczby):
    tab = [[int(i),False] for i in str(liczby)]
    tab.reverse()
    wyniki = []

    dasie = True
    
    while dasie == True:

        for i in range(len(tab)-1):
            if tab[i] == tab[i+1] and tab[i][1] == False:
                tab[i] = 0
                tab[i+1][0] = (tab[i+1][0]*2)%10
                tab[i+1][1] = True

        tab = [i for i in tab if i != 0]

        licznik = 1
        for i in range(len(tab)-1):
            tab[i][1] = False
            if tab[i][0] != tab[i+1][0]:
                licznik+=1
                
        if licznik == len(tab):
            dasie = False

    for i in range(len(tab)):
        wyniki.append(str(tab[i][0]))

    wyniki.reverse()
    
    return int(''.join(wyniki))        
        
print(
redukcja(84211)
)
