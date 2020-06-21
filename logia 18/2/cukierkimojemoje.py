def ilerazy(n, tab):
    wyniki = [0]
    worek = 0
    
    for i in range(len(tab)):
        if i%2 ==0:
            for j in range(tab[i]):
                worek+=1
                wyniki.append(worek)
        else:
            for j in range(tab[i]):
                worek-=1
                wyniki.append(worek)
                

    return len([i for i in wyniki if i == n])

print(
ilerazy(2, [3, 2]),
ilerazy(4, [5, 3, 5, 3, 2, 1])
)
