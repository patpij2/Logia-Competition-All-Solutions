def ms(n,dzialki):
    wyniki = []
    wypisz = []
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if not (i-1)*n+j in dzialki:
                sasiedzi = 0
                if i > 1:
                    if (i-2)*n+j in dzialki:
                        sasiedzi+=1
                if i < n:
                    if (i)*n+j in dzialki:
                        sasiedzi+=1
                if j < n:       
                    if (i-1)*n+j+1 in dzialki:
                        sasiedzi+=1
                if j > 1:       
                    if (i-1)*n+j-1 in dzialki:
                        sasiedzi+=1
                wyniki.append(sasiedzi)

    maksimum = max(wyniki)

    for i in range(1,n+1):
        for j in range(1,n+1):
            if not (i-1)*n+j in dzialki:
                sasiedzi = 0
                if i > 1:
                    if (i-2)*n+j in dzialki:
                        sasiedzi+=1
                if i < n:
                    if (i)*n+j in dzialki:
                        sasiedzi+=1
                if j < n:       
                    if (i-1)*n+j+1 in dzialki:
                        sasiedzi+=1
                if j > 1:       
                    if (i-1)*n+j-1 in dzialki:
                        sasiedzi+=1
                if sasiedzi == maksimum:
                    wypisz.append((i-1)*n+j)
                
    return wypisz

print(
ms(4,[9,10,14]),
ms(3,[4,5,6])
)
