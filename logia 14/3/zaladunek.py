def ilesam(partie, ciezarowki):

    ciezarowka = 0
    for p in partie:
        for i in range(int(p[0])):
            if ciezarowki[ciezarowka]-p[1] >= 0:
                ciezarowki[ciezarowka] -= p[1]
            else:
                ciezarowka +=1
                ciezarowki[ciezarowka] -= p[1]

    print(ciezarowka+1)

ilesam([[4, 5], [2, 2], [1, 20]], [17, 25, 25, 17, 25])
ilesam([[20, 1],[2, 5],[1, 3],[2, 7]], [25, 10, 10, 10, 10, 10])
