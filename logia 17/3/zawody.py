def zawody(tab):
    alfa = [chr(i).capitalize() for i in range(97, 123-(26-len(tab[0])))]

    for runda in tab:
        minimum = min(runda)
        do_wyrzucenia = runda.index(minimum)

        alfa.pop(do_wyrzucenia)

    return alfa[0]


print(
zawody([[4,0,2,1],[1,2,3],[2,1]]),
zawody([[8,9]])
)
