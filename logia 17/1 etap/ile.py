def jest13(a):
    licznik = 0
    for i in range(len(a)-1):
        if a[i:i+2] == '13':
            licznik += 2
    return licznik

def ile(n):
    licznik=0
    for i in range(1, n+1):
            licznik += jest13(str(i))
            #if jest13(str(i))>0:
            #    print(i)
    return licznik

'''
def ile2(n):
    licznik=0
    for i in range(1, n+1):
            licznik += str(i).count("13")*2
    return licznik
'''

print( ile(199) )
