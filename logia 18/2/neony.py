def neon(tab):

    wyniki=[]
    for dalejtab in range(len(tab)):
        for dlakazdego in range(len(tab)-dalejtab):
            if dalejtab!=dlakazdego:
                ocena=tab[dalejtab]+tab[dlakazdego]+(abs(dalejtab-dlakazdego)*2)
                wyniki.append(ocena)
    print(max(wyniki))


neon([10, 4, 5, 7, 1, 4, 1])
#neon([1, 10, 1])
