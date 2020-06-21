import numpy as np

def obok(n,k):
    tab = np.array([i for i in range(1,n**3+1)])
    tab = tab.reshape((n,n,n))
    #print(tab)

    wyniki = []
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if tab[x][y][z] == k:
                    if x < n-1 :
                        wyniki.append(tab[x+1][y][z])
                    if x > 0 :    
                        wyniki.append(tab[x-1][y][z])
                    if y < n-1 :
                        wyniki.append(tab[x][y+1][z])
                    if y > 0 :
                        wyniki.append(tab[x][y-1][z])
                    if z < n-1 :
                        wyniki.append(tab[x][y][z+1])
                    if z > 0 :
                        wyniki.append(tab[x][y][z-1])
    return list(np.sort(wyniki))

print(
obok(3, 11),
obok(7, 1),
obok(10, 1000)
)
