import time
def liczby(tab):
    wynikiost = []
    for liczba in tab:
    
        wyniki = []
        for i in range(liczba+1):
            for j in range(liczba+1):
                if i*j == liczba:
                    wyniki.append([j,i])


        wyniki1 = []
        for i in wyniki:
            wyniki1.append(abs(i[0] - i[1]))
                
        wynikiost.append([wyniki[wyniki1.index(min(wyniki1))][1],wyniki[wyniki1.index(min(wyniki1))][0]])

    print(wynikiost)



def liczby2(tab):
    wynikiost = []
    for liczba in tab:

        minimum = liczba
        x = 0

        y = 0
        for i in range(1,(liczba+1)//2+1):
            if liczba % i == 0:
                j = liczba // i
                if abs(i-j) >= minimum:
                    break
                else:
                    minimum = abs(i-j)
                    x = i
                    y = j
                
        wynikiost.append([x,y])

    print(wynikiost)
'''
t1 = time.time()
#liczby([13,44,42])               
#liczby([12,7,10,24])
liczby([10000])

t2 = time.time()

print('pierwszy: ',t2-t1)
'''

t1 = time.time()
#liczby2([13,44,42])               
liczby2([12,7,10,24])
liczby2([10**9])

t2 = time.time()

print('drugi: ',t2-t1)
