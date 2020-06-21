def ms(n,tab):
    ls = []
    for i in range(1,n**2+1):
        lsn = 0
        if i - n >= 0:
            if i-n in tab:
                lsn += 1
                
        if i+n <= n**2:
            if i+n in tab:
                lsn += 1
                
        if (i-1) % n > 1:
            if i-1 in tab:
                lsn += 1
                
        if i % n != 0:
            if i+1 in tab:
                lsn += 1

        if i in tab:
            lsn = 0
        ls.append(lsn)

    return [ i for i in range(1,n**2+1) if ls[i-1] == max(ls)]
        

print(
ms(4,[9,10,14]),
ms(3,[4,5,6]),
ms(5,[1,7,13,19,25])
)
