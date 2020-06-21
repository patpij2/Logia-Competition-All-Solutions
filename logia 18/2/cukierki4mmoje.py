def ilerazy(n, tab):
    torba = 0
    oldtorba = 0
    licznik = 0

    for i in range(len(tab)):
        if i%2 == 0:
            torba+=tab[i]
            if oldtorba < n <= torba:
                licznik+=1
        else:
            torba-=tab[i]
            if oldtorba > n >= torba:
                licznik+=1
        oldtorba = torba


    print(licznik)


ilerazy(4, [5, 3, 5, 3, 2, 1])           
#ilerazy(2, [3, 2])
