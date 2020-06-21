def good(tab):
    for i in range(len(tab)):
        if tab[i] == 'c' and 'z' in tab[:i-1]:
            return False

    return True

def good2(tab):
    for i in range(len(tab)):
        if tab[i] == 'n' and ('z' in tab[:i-1] or 'c' in tab[:i-1]):
            return False

    return True

def abc(napis):
    tab = [i for i in napis]
    i = 0

    while i < len(tab):
            if good2(tab[:i+1]):
                i+=1
            else:
                liczba_zc = tab[:i+1].count('z')+tab[:i+1].count('z')
                liczba_z = tab[:i+1].count('z')
                liczba_c = tab[:i+1].count('c')

                liczba_n = tab[i:].count('n')
                #print(liczba_c, liczba_z, tab[i:].index('z'), tab[i:i+ tab[i:].index('z')])

                if liczba_zc < liczba_n:
                    for j in range(liczba_z):
                        tab.remove('z')
                    for j in range(liczba_c):
                        tab.remove('c')
                    i = 0
                    
                else:
                    tab.pop(i)
                    #print('dsd')
    i=0

    while i < len(tab):
        if good(tab[:i+1]):
            i+=1
        else:
            liczba_z = tab[:i+1].count('z')
            liczba_c = tab[i:].count('c')
            #print(liczba_c, liczba_z, tab[i:].index('z'), tab[i:i+ tab[i:].index('z')])

            if liczba_z < liczba_c:
                for j in range(liczba_z):
                    tab.remove('z')
                i = 0
                
            else:
                tab.pop(i)
                #print('dsd')


    return tab

print(
#abc('zzzzcccc')
abc('n')
)
