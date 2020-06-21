def ilerazy(n,tab):
    wyniki = [0]
    aktualne = 0
    for i in range(len(tab)):
            for j in range(tab[i]):
                if i%2 == 0:
                    aktualne +=1
                else:
                    aktualne -=1
                wyniki.append(aktualne)

    return wyniki.count(n)

print(
ilerazy(4, [5, 3, 5, 3, 2, 1]),
ilerazy(2, [3, 2])
)

