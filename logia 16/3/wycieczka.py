def dziel(m,k,wyniki):
    if len(k) > 1:
        i=k.index(m[0])
        dziel(m[1:i+1],k[0:i],wyniki)
        dziel(m[i+1:], k[i+1:],wyniki)
        wyniki.append(k[i])
        
    elif len(k)==1:
        wyniki.append(k[0])


def opis(m,k):
    wyniki = []
    dziel(m,k,wyniki)

    print(wyniki)

opis([4,2,1,3,5,6],[1,2,3,4,6,5])
opis([1,2,4,5,3,6,7],[4,2,5,1,6,3,7])
opis([1,2,4,3],[4,2,1,3])
