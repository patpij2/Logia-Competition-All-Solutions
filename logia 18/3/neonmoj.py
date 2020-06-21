def neon(tab):
    maks = 0
    for x1 in range(len(tab[0])):
        for y1 in range(len(tab[0])):
            for x2 in range(len(tab[0])-x1):
                for y2 in range(len(tab[0])-y1):
                    odleglosc = abs(x1-x2)+abs(y1-y2)
                    maks = max(tab[x1][y1]+tab[x2][y2]+(odleglosc*2), maks)
    return maks

print( neon([[1,2,1,2],[7,1,7,1],[1,1,1,1],[3,3,3,3]]) )
print( neon([[1, 9, 2],[3, 8, 3],[2, 1, 1]]) )
