def wzorek(h,napis):
    tab = [[0 for i in range(h)] for j in range(len(napis)//h)]

    licznik = 0
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            tab[i][j] = napis[licznik]
            licznik +=1

    maksi = 0

    for i in tab:
        maksi = max(maksi,i.count('1'))
    print(maksi)

    for i in tab:
        if i.count('1') == maksi:
            for j in range(len(tab[0])):
                if i[j] == '1':
                    i[j] = '2'

    for i in tab:
        print(i)
        
#wzorek(2, '10111001011011')
wzorek(3, '000000000000000000101')
#wzorek(3, '101010111010101010111')
#wzorek(5, '10001011101000101010')  
