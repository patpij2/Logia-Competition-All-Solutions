def o6(n):
    tab = [i for i in range(n+1)]

    #SITO
    for j in range(2, n+1):
        if tab[j]!=0:
            for i in range(2*tab[j],n+1,tab[j]):
                tab[i] = 0
                
    tab = [i for i in tab if i!=0 and i!=1]


    #SZUKANIE
    wyniki = []
    for i in range(len(tab)):
        for j in range(len(tab)):
            if abs(tab[j]-tab[i]) == 6 and max(tab[j],tab[i])<n:
                wyniki.append(max(tab[j],tab[i]))

    return(max(wyniki))
            
