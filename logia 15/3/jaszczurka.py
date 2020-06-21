def droga(tab):
    newtab = []
    wynik = 0
    wynik1 = 0
    
    for i in tab:
        if type(i) == int:
            newtab.append([i,0])
        else:
            newtab.append(i)

    for i in range(len(newtab)):
        wynik+=newtab[i][0]

    for i in range(len(newtab)-1):
        wynik1+=abs(newtab[i][1]-newtab[i+1][1])

        

    print(wynik+wynik1+newtab[0][1]+newtab[-1][1])


#droga([[40,20],[50,30],10,[20,20],20,[40,10]])
droga([10,10,[20,10],10])
