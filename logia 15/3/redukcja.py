def obrot(tab,n):
    tab = [[tab[n-j-1][i] for j in range(n)] for i in range(n)]
    #[[print(tab[i][j], end= ' ') for i in range(n)] and print() for j in range(n)]   
    return tab

def spadanie(tab,n):
    for k in range(n):
        for i in range(n):
            for j in range(n-1):
                if tab[i][j] != 0 and tab[i][j+1] == 0:
                    tab[i][j],tab[i][j+1] = tab[i][j+1],tab[i][j]
    return tab

def redukuj(tab,n):
    for k in range(n):
        for i in range(n):
            for j in range(n-1):
                if tab[i][j] == tab[i][j+1]:
                    tab[i][j] = (tab[i][j]*2)%10
                    tab[i][j+1] = 0
                    tab = spadanie(tab,n)
    return tab
                
def redukcja(tab,napis):
    n=len(tab)
    tab = [[tab[i][j] for i in range(n)] for j in range(n)]
    
    [[print(tab[i][j], end= ' ') for i in range(n)] and print() for j in range(n)]
    print()
    
    for znak in napis:
        if znak == 'l':
            tab = obrot(tab,n)
        if znak == 'p':
            tab = obrot(tab,n)
            tab = obrot(tab,n)
            tab = obrot(tab,n)
        if znak == 'g':
            tab = obrot(tab,n)
            tab = obrot(tab,n)
        #[[print(tab[i][j], end= ' ') for i in range(n)] and print() for j in range(n)]
        #print()   
        tab = spadanie(tab,n)
        tab = redukuj(tab,n)

        if znak == 'p':
            tab = obrot(tab,n)
        if znak == 'l':
            tab = obrot(tab,n)
            tab = obrot(tab,n)
            tab = obrot(tab,n)
        if znak == 'g':
            tab = obrot(tab,n)
            tab = obrot(tab,n)
        #[[print(tab[i][j], end= ' ') for i in range(n)] and print() for j in range(n)]
        #print()
    tab = [[tab[i][j] for i in range(n)] for j in range(n)]
    
    return tab

print(
redukcja([[0,2,4],[4,4,8],[4,0,8]],'dldld'), '\n',
redukcja([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]],'lpdg')
)
