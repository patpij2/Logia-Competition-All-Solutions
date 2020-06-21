def kolit(a):
    napis = [i for i in a]
    print(napis)
    krok=1
    j=1
    while len(napis)>0:
        while j<len(napis):
            print(j, '),', krok,'     ', napis[j], '    ', napis[j+krok])
            j+=krok
            krok+=1
            
