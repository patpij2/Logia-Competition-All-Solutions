def nrj(tab):
    tab1 = []
    tab2 = []
    wyniki = []

    for i in tab:
        napis = str(i[1])
        minuty = int(napis[-2:])

        if len(napis) == 3:
            godzina = int(napis[0])
        else:
            godzina = int(napis[0:2])
            
        czas = godzina*60 + minuty

        if i[0] == 1:
            tab1.append(czas)
        else:
            tab2.append(czas)

    new_tab1 = []
    new_tab2 = []
    for i in range(len(tab1)-1):
        new_tab1.append((tab1[i]+tab1[i+1])//2)
    for i in range(len(tab2)-1):
        new_tab2.append((tab2[i]+tab2[i+1])//2)

    tab1.extend(new_tab1)
    tab2.extend(new_tab2)

    for i in range(1440):
        if i in tab1 and i in tab2:
            wyniki.append([2, i-1])
            wyniki.append([1, i])          
        elif i in tab1:
            wyniki.append([1, i])
        elif i in tab2:
            wyniki.append([2, i])

    for i in range(len(wyniki)):
        godz = wyniki[i][1]//60
        minuty = wyniki[i][1]%60

        wyniki[i][1] = godz*100+minuty 
    
    return wyniki

print(
nrj([[1,700],[2,707],[1,720]]),
nrj([[1,701],[2,710],[1,715],[2,720]])
)
