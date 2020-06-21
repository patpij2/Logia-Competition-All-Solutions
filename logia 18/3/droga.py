def droga(tab):
    A = ['A']
    Z = ['Z']

    for j in range(26):
        for i in range(len(tab)):
            if tab[i][0] == A[-1]:
                A.append(tab[i][1])
                break
        for i in range(len(tab)):
            if tab[i][0] == Z[-1]:
                Z.append(tab[i][1])
                break

    koszty = []
    for i in range(len(Z)):
        if Z[i] in A:
            koszty.append(i+A.index(Z[i]))

    if len(koszty) == 0:
        return -1

    else:
        return(min(koszty))


print(
droga([['Z', 'D'], ['A', 'B'], ['F','B'],['B','C'],['C','D'],['D','F']]),
droga([['A','B'],['G','H'], ['B','C'],['Z','C']]),
droga([['A', 'B'], ['Z','D']])
)
