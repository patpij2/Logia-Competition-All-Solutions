def szyfr(slowo, klucz):
    wyniki = ''
    for i in range(0,len(slowo),2):
        liczba = (ord(slowo[i])-97) * 26 + (ord(slowo[i+1])-97)
    
        liczba += klucz

        liczba = liczba % 676

        wyniki += chr(liczba//26 + 97) + chr(liczba%26 +97)

    print(wyniki)

szyfr('abrakadabraa',500)
szyfr('dzisiajjestkonkurs', 487)
