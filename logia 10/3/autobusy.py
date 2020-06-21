def droga(linie, p1, p2):
    wyniki = []

    for l in linie:
        if p1 in l and p2 in l:
            wyniki.append(abs(l.index(p1)- l.index(p2)))

    if len(wyniki) > 0:
        return min(wyniki)
    else:
        return -1


print(
droga([[4,3,2,1,],[3,2]],2,3),
droga([[2,4,3,1],[4,2,1,3]],2,1),
droga([[1,2,3,4,5],[6,5,4,9,8,5,2],[1,6,5,8,9]],1,5)
)
