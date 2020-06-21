def abc(korale):
    korale = [[i] for i in korale]
    
    for i in range(len(korale)-1):
        if korale[i] == korale[i+1]:
            korale[i]+=korale[i+1]
            korale[i+1] = 0
            
    korale = [i for i in korale if i != 0]

    for i in range(len(korale)-1):
        if korale[i][0] == korale[i+1][0]:
            korale[i].extend(korale[i+1])
            korale[i+1] = [0]
            
    korale = [i for i in korale if i != [0]]

    for i in range(len(korale)-1):
        if korale[i][0] == korale[i+1][0]:
            korale[i].extend(korale[i+1])
            korale[i+1] = [0]
            
    korale = [i for i in korale if i != [0]]





    print(korale)
    
abc('nncnnbffbbbbbbccczzzcz')
