def obok(n,k):
    tab = [[[n**2*v+n*j+i+1 for i in range(n)] for j in range(n)] for v in range(n)]
    wyniki = []

    for i in range(n):
        for j in range(n):
            for v in range(n):
                if tab[i][j][v] == k:
                    if i > 0:
                        wyniki.append(tab[i-1][j][v])
                    if i < n-1:
                        wyniki.append(tab[i+1][j][v])
                        
                    if j > 0:
                        wyniki.append(tab[i][j-1][v])
                    if j < n-1:
                        wyniki.append(tab[i][j+1][v])
                        
                    if v > 0:
                        wyniki.append(tab[i][j][v-1])
                    if v < n-1:
                        wyniki.append(tab[i][j][v+1])

    wyniki.sort()
    print(wyniki)

obok(3, 11)	
obok(10, 1000)	   
obok(7, 1)
