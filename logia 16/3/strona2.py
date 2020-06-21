def maxu(czas):
    t = [czas[i][0] for i in range(len(czas))]
    start = min(t)
    t2 = [czas[i][1] for i in range(len(czas))]
    koniec = max(t2)+max(t)
    tab = [0 for i in range(0,koniec)]
    
    print(start, koniec, tab)
    
    for i in range(len(czas)):
        for j in range(czas[i][0],czas[i][0]+czas[i][1]+1):
            tab[j-start]+=1

    return(tab)  

print(
maxu([[1,2],[2,3],[1,10],[2,2],[5,5]])
)
