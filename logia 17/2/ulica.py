def maksos(tab):

    for i in range(len(tab)):
        for j in range(len(tab)):
            if abs(tab[i]-tab[j])<=3 and tab[i]!=tab[j]:
                print(tab[j])z


maksos([1,4,7,11,13,14,15,16,20])
