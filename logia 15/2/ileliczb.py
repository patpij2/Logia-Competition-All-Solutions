def ile(a,b):
    i=0
    licznik=0
    for i in range(0, a**10+100):
        if str(b) in str(i) and len(str(i))==a:
            licznik+=1
            #print(i)

    return licznik
        
        
print(
ile(1,4),
ile(2,5),
ile(3,6)
)
