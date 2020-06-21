def liczby(tab):
    wyniki = []

    for liczba in tab:
        a = 1
        b = liczba
        mini = liczba-1
        for i in range(2, liczba+1):
            if liczba%i == 0:
                roznica = abs(i-liczba//i)
                #print(roznica,mini)
                if roznica < mini :
                    mini = roznica
                    a = i
                    b = liczba//i

        if a>b:
            wyniki.append([b,a])

        else:
            wyniki.append([a,b])

    return wyniki

print(
liczby([4,25,46,33]), ' ---',        
liczby([1233333,7,10,24]),' ---', 
liczby([13,44,42])
#liczby([12])
)
