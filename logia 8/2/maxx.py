def maxx(slowo):
    maxdl = 0
    maxsl = ''
    for i in list(set([i for i in slowo])):
        #print(abs( slowo.index(i) - ( len(slowo) - slowo[::-1].index(i) ) ))
        if int(abs( slowo.index(i) - ( len(slowo) - slowo[::-1].index(i) ) ) ) > maxdl:
            maxdl = int(abs( slowo.index(i) - ( len(slowo) - slowo[::-1].index(i) ) ))
            maxsl = slowo[slowo.index(i):( len(slowo) - slowo[::-1].index(i) )]
    print(maxsl)
    
slowo = 'abc'
for i in range(1000):
    slowo1 = 'abc'
    slowo2 = 'abc'
    slowo3 = 'abc'
    maxx(slowo)
    maxx(slowo1)
    maxx(slowo2)
    maxx(slowo3)
    
            

