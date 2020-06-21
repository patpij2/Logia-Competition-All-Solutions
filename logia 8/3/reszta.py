def reszta(k,m):
    tab = [0 for i in range(k+1)]

    for i in range(1,k+1):
        mini = float('inf')

        for j in m:
            if i >= j:
                mini = min(mini,tab[i-j])

        tab[i] = mini+1

    print(tab)


reszta(6,[1,2])
