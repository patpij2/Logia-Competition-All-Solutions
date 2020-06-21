def pokolenia(tab):
    osoby = list(set([tab[i][j] for i in range(len(tab)) for j in range(2)]))

    glowa = ''
    for os in osoby:
        for i in tab:
            udalosie = True
            if i[1] == os:
                udalosie = False
                break
        if udalosie:
            glowa = os

    rodzina = [[glowa]]

    while True:
        pok = []
        for j in rodzina[-1]:
            
            for i in tab:
                if i[0] == j:
                    pok.append(i[1])

        if len(pok) == 0:
            break
        else:
            rodzina.append(pok)

    for pok in rodzina:
        pok.sort()

    rodzina[0] = rodzina[0][0]

        
    print(rodzina)
    

pokolenia([["a", "b"], ["b", "x"], ["a", "d"], ["a", "z"]])

pokolenia([["Ula", "Ala"], ["Ola", "Ula"], ["Ela", "Ola"], 
["Ela", "Jan"]])
