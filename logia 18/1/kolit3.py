def kolit(napis):
    napis = [i for i in napis]
    suma = 0
    wys = 1
    if len(napis) > 1:
        for i in range(len(napis)):
            if suma >= len(napis):
                while len(napis) != suma:
                    napis.append(0)
                wys = i
                break
            suma += i

    piramida = [[]]
    for i in range(wys):
        
        for j in range(len(napis)):
            if napis[j] != 0:
                piramida[i].append(napis[j])
                napis[j] = 0
            if len(piramida[i]) == i+1:
                break
        piramida.append([])

    piramida = [i for i in piramida if len(i) != 0]

    maksi = -float('inf')
    for i in piramida:
        maksi = max(maksi,len(i))


    for i in range(len(piramida)):
        while len(piramida[i]) != maksi:
            piramida[i].append(0)

    licznik = 0
    for i in range(len(piramida[0])):
        tmp = []
        for j in range(len(piramida)):
            tmp.append(piramida[j][i])

        tmp = [i for i in tmp if i != 0]
        if len(tmp) == tmp.count(tmp[0]):
            licznik +=1

    return licznik
        
   
print(kolit('ALAMAKRABY'))
