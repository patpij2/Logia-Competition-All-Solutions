def kolit(slowo):
    licznik = 0

    while len(slowo) > 0:
        napis = ''
        i = 0
        krok = 1
        while i < len(slowo):
            napis += slowo[i]
            slowo = slowo[:i] + '0' + slowo[i+1:]
            i += krok
            krok += 1

        slowo = slowo.replace('0','')
        if napis.count(napis[0]) == len(napis):
            licznik += 1

    return licznik

            
            
