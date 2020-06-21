def kolit(napis):
    napis = [i for i in napis]
    tab = []

    licznik = 0
    i = 0
    j = 0
    while i < len(napis):
        i += 1
        j += i
        tab.append(napis[licznik:j])
        licznik = j

    tab = [i for i in tab if len(i) != 0]

    maksi = -100000
    for i in tab:
        maksi = max(maksi,len(i))

    for i in range(len(tab)):
        while len(tab[i]) < maksi:
            tab[i].append(0)


    wyniki = 0
    for i in range(len(tab[0])):
        tmp = []
        for j in range(len(tab)):
            tmp.append(tab[j][i])
        tmp = [i for i in tmp if i != 0]
        if tmp.count(tmp[0]) == len(tmp):
            wyniki+=1

    return wyniki

print(
kolit('ABCDEFGH')
)
