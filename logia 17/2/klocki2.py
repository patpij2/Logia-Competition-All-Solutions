def kolit(slowo):
    i=0
    j=1
    tab = []

    while i<=len(slowo):
        tab.append(slowo[i:i+j])
        j+=1
        i+=j-1
        
    for i in range(len(tab)):
        tab[i]=tab[i].ljust(len(tab[-2])+1,'0')

    tab = [[tab[j][i] for j in range(len(tab[0])) if tab[j][i] !='0'] for i in range(len(tab))]
    
    if len(tab[-1]) == 0:
        tab.pop(-1)

    licznik = 0

    for i in tab:
        if len(i) == i.count(i[0]):
            licznik+=1

    

    return licznik

print(    
kolit('ALAMAKRABY'),
kolit('ABCDEFGH')
)
