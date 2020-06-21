def ilecyfr(liczba, podstawa):
    licznik = 0 
    while liczba > 0:
        licznik+=1
        liczba = int(liczba/podstawa)
    print(licznik)

ilecyfr(123456, 10)
ilecyfr(1, 5)
ilecyfr(255, 2)
ilecyfr(255, 16)
ilecyfr(1000000000000000000, 17)
