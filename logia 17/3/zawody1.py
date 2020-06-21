def zawody(tab):
    zawodnicy = [chr(i).capitalize() for i in range(97,97+len(tab[0]))]

    for runda in tab:
        zawodnicy.pop(runda.index(min(runda)))

    return zawodnicy[0]

print(
zawody([[8,9]]),
zawody([[4,0,2,1],[1,2,3],[2,1]])
)
