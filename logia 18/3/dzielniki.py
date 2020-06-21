def dzielniki(a,b):
    licznik = 0

    for i in range(a,b+1):
        if int(i**0.5)**2 == i: 
            dzielniki = 1
            for j in range(1,i//2+1):
                if dzielniki > 3:
                    break
                if i % j == 0:
                    dzielniki+=1

            if dzielniki == 3:
                licznik +=1
            
        
    return licznik

print(
dzielniki(2, 6),
dzielniki(80000,90000)
#dzielniki(1,1000000)
)
