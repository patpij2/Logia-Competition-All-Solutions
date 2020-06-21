def ilesam(p, c):
    paczki = []

    for i in range(len(p)):
        for j in range(p[i][0]):
            paczki.append(p[i][1])

    nrc = 0
    for paczka in paczki:
        if c[nrc] >= paczka:
            c[nrc] -= paczka

        else:
            nrc += 1
            c[nrc] -= paczka

    return nrc+1


print(
ilesam([[4, 5], [2, 2], [1, 20]], [17, 25, 25, 17, 25]),
ilesam([[20, 1],[2, 5],[1, 3],[2, 7]], [25, 10, 10, 10, 10, 10])

)
