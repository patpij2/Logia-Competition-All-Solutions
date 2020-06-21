def ilerazy(n, tab):
    torba = 0
    wyniki = []

    for i in range(len(tab)):
        if i%2==0:
            for j in range(tab[i]):
                torba+=1
                wyniki.append(torba)
                
        else:
            for j in range(tab[i]):
                torba-=1
                wyniki.append(torba)

    print(wyniki.count(n))


ilerazy(4, [5, 3, 5, 3, 2, 1])           
#ilerazy(2, [3, 2])
