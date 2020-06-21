def kostka(wartosc_k, wybor):
    tab = [i+1 for i in range(6)]

    tab.remove(wartosc_k)
    tab.remove(7-wartosc_k)

    if wybor == "max":
        return max(tab)
    
    else:
        return min(tab)

def gra(kosc, moneta, limit):
    liczba_graczy = len(moneta[0])
    liczba_tur =len(moneta)
    
    wyniki = []

    for gracz in range(liczba_graczy):
        licznik_punktow = 0
        wartosc_k = kosc
        
        for tura in range(liczba_tur):
            if moneta[tura][gracz] == 'o':
                wartosc_k = kostka(wartosc_k, 'max')
                licznik_punktow += wartosc_k

            else:
                wartosc_k = kostka(wartosc_k, 'min')
                licznik_punktow += wartosc_k

            if licznik_punktow >= limit:
                wyniki.append(tura+1)
                break
            
        if len(wyniki) == gracz:
            wyniki.append(0)
                
    return wyniki



print(
gra(4, [['o','r','r'],['r','o','r']],5),
gra(4, [['o'],['r'],['r']],7),
gra(4, [['o','r'],['r','r'],['r','o']],7)



)
