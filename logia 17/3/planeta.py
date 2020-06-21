def odleglosc(dom, dom2, n):
    x1 = abs(dom[0]-dom2[0])
    x2 = abs(n-x1)
    x = min(x1,x2)

    y1 = abs(dom[1]-dom2[1])
    y2 = abs(n-y1)
    y = min(y1,y2)

    return x+y

def planeta(n,tab):
    nr = [0 for i in tab]
    
    for dom in tab:
        for dom2 in tab:
            if dom != dom2 and odleglosc(dom,dom2,n) <=5:
                if nr[tab.index(dom)] == 0 and nr[tab.index(dom2)] == 0:
                    nr[tab.index(dom)] = max(nr)+1
                    nr[tab.index(dom2)] = max(nr)+1
                    
                elif nr[tab.index(dom)] == 0:
                    nr[tab.index(dom)] = nr[tab.index(dom2)]

                else:
                    nr[tab.index(dom2)] = nr[tab.index(dom)]


    for i in range(len(nr)):
        if nr[i] == 0:
            nr[i] = max(nr)+1

    maksimum = 0

    for i in range(len(nr)):
        if maksimum < nr.count(nr[i]):
            maksimum = nr.count(nr[i])
    

    return maksimum


print(
planeta(12,[[3,1],[1,1],[1,3],[2,12],[9,5],[8,6]])
#planeta(100,[[6,6],[6,11],[11,6],[11,11],[80,80]])
)
