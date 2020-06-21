def ilen(n,mapa):
    tab = [[1 for i in range(n)] for j in range(n)]
   
    for k in range(len(mapa)):
        for j in range(mapa[k][1],mapa[k][3]):
            for i in range(mapa[k][0],mapa[k][2]):
                tab[j][i] = mapa[k][4]

    for i in range(len(tab)):
        tab += tab[0]
        tab.remove(tab[0])
        
    return [tab.count(1),tab.count(2),tab.count(3)]

print(
ilen(4,[[0,0,1,2,2],[0,1,3,2,2],[3,3,4,4,3]]),
ilen(4,[[0,0,4,4,2]]),
ilen(3,[[0,0,1,1,3],[2,2,3,3,2]])
)
