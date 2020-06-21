def neon(tab):

    wyniki = []
    for i in range(len(tab)):
        for j in range(len(tab)-i):
            if tab[i] != tab[j]:
                naj = tab[i]+tab[j]+abs(i-j)*2
                wyniki.append(naj)
            
    return max(wyniki)

print(
neon([10, 4, 5, 7, 1, 4, 1]),
neon([1, 10, 1])
)
