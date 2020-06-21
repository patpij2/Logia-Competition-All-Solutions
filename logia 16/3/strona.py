def maxu(tab):
    wyniki = []
    mini = tab[0][0]
    maxi = tab[0][0] + tab[0][1]
    
    for i in tab:
        mini = min(i[0], mini)
        maxi = max(i[1]+i[0], maxi)

    for t in range(mini, maxi+1):
        lu = 0
        for l in tab:
            if l[0] <= t <= l[0]+l[1]:
                lu +=1
        wyniki.append(lu)

    return max(wyniki)
            
print(
maxu([[1,2],[2,3],[1,10],[2,2],[5,5]]),
maxu([[1,10],[2,8],[3,6]]),
maxu([[1,2],[2,2]])
)
