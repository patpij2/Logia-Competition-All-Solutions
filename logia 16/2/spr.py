def ok(napis):
    tab = [i for i in napis]
    
    for i in range(len(tab)):
        if tab[i]=='a':
            for j in range(i,len(tab)):
                if tab[j] == 'b':
                    tab[i],tab[j]=0,0
                    break
    if tab.count('a') > 0 or tab.count('b') > 0:
        return False
    else:
        return True
            
            
def spr(napis):
    
    for i in range(len(napis)-1, -1 ,-1):
        if ok(napis[0:i+1]):
            return i+1
    return 0



print(
spr('abrakadabra'),
spr('balon'),
spr('arbuz')
)
