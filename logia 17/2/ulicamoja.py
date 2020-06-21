def maksos(tab):
    osiedla = [[]]
    kolejne_osiedle = 0
    maks = -1000000
    for i in range(len(tab)-1):
        if abs(tab[i+1]-tab[i]) <= 3:
            osiedla[kolejne_osiedle].append(tab[i])
        else:
            osiedla[kolejne_osiedle].append(tab[i])
            kolejne_osiedle +=1
            osiedla.append([])

    if len(osiedla[-1]) == 0:
        osiedla.pop(-1)

    if abs(tab[-1] - osiedla[-1][-1]) <=3:
        osiedla[-1].append(tab[-1])
    else:
        osiedla.append([tab[-1]])

    if osiedla[0][0] <=3 and len(osiedla) > 1:
        osiedla[0] = osiedla[-1] + osiedla[0]
        osiedla.pop(-1)

    print(osiedla)

    for i in osiedla:
        maks = max(len(i), maks)
    
    print(maks)
            

maksos([1,4,7,11,13,14,15,16,27])
maksos([1,4,7,13,14,15,20])

maksos([1,4,7,8,13,14,15,20,30,33,34,35])
