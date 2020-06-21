def perm(tab,k):
    wyniki = []
    if k == 0:
        wyniki.append(tab.copy())
    else:
        for i in range(k):
            tab[i],tab[k-1] = tab[k-1],tab[i]
            wyniki.extend( perm(tab,k-1) )
            tab[i],tab[k-1] = tab[k-1],tab[i]
    return wyniki


def kulki(r,g,b,y):
    lancuch = 'r'*r + 'g'*g + 'b'*b + 'y'*y
    lancuch = [i for i in lancuch]
    dl = r+g+b+y
    
    tabperm = perm(lancuch,dl)
    wyniki = []
 
    for i in tabperm:
        good = True
        for j in range(len(i)-1):
            if i[j] == i[j+1]:
                good = False
        if good:
            wyniki.append(''.join(i))
    
    wyniki = list(set(wyniki))

    print(sorted(wyniki))
        
    

kulki(2,1,1,0)

