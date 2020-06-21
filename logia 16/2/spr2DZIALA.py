def ok(slowo):
    tab = [i for i in slowo]

    for i in range(len(tab)):
        if tab[i] == 'a':
            for j in range(i,len(tab)):
                if tab[j] == 'b':
                    tab[i],tab[j] = 0,0
                    break
                
    if tab.count('a') > 0 or tab.count('b') > 0:
        return False
    return True

def spr(slowo):
    
    for i in range(len(slowo)-1,-1,-1):
        if ok(slowo[0:i+1]):
            return i+1
    return 0
