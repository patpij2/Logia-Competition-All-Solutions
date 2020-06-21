import time

def anagramy(wyrazy):
    slowa = []
    for slowo in wyrazy:
        slowa.append( sorted([i for i in slowo]) )

    wyniki = [[]]
    n = 0
    for i in range(len(slowa)):
        wyniki[n].append(wyrazy[i])
        for j in range(len(slowa)):
            if slowa[i] == slowa[j] and i != j:
                wyniki[n].append(wyrazy[j])
                
        wyniki.append([])
        n += 1
        

    wyniki = [sorted(i) for i in wyniki if len(i) != 0]

    for lista in wyniki:
        while wyniki.count(lista) > 1:
            wyniki.remove(lista)

    
    return sorted(wyniki)

###############################

def perm(tab,k):
    wyniki = []
    if k == 0:
        wyniki.append(tab.copy())
    else:
        for i in range(k):
            tab[i],tab[k-1] = tab[k-1],tab[i]
            wyniki.extend(perm(tab,k -1))
            tab[i],tab[k-1] = tab[k-1],tab[i]

    return wyniki

def anagramy_perm(wyrazy):
    wyniki = [[]]
    
    n = 0
    for slowo in wyrazy:
        if slowo != 0:
            tabslowo = [i for i in slowo]
            lentab = len(tabslowo)
            permtab = perm(tabslowo,lentab)
            
            for permslowo1 in permtab:
                permslowo = ''.join(permslowo1)
                
                if permslowo in wyrazy:
                    wyniki[n].append(''.join(permslowo))
                    wyrazy[wyrazy.index(permslowo)] = 0
            
        wyniki.append([])            
        n+=1                

    wyniki = [sorted(i) for i in wyniki if len(i) != 0 ]
    
    return wyniki


a = time.clock()

anagramy(['kto','tyran','kra','kot','pies','tok','narty','rak'])

b = time.clock()

print('anagramy bez permutacji: ', b-a)

#############

a = time.clock()

anagramy_perm(['kto','tyran','kra','kot','pies','tok','narty','rak'])

b = time.clock()

print('anagramy z permutacja: ', b-a)

