def plot(keys, matrix):
    print("  ",end="")
    for i in keys:
        print(i,end=" ")
    print()
    for i in keys:
        print(i,end=" ")
        for j in keys:
            print(matrix[i][j], end = ' ')
        print()
    print()

def chodzenie(s,keys,matrix,d,licznik,znaleziono):
    #print(s,d)
    if s == d:
        #print('hay!')
        znaleziono.append(licznik)
    else:
        for i in keys:
            if matrix[s][i] > 0:
                tmp = matrix[s][i]
                matrix[s][i] = 0
                chodzenie(i,keys,matrix,d,licznik+tmp,znaleziono)
                matrix[s][i] = tmp

def kosp(napis1, napis2):
    napis1 += 'C'
    napis2 += 'C'
    keys1 = [napis1[i] for i in range(0,len(napis1),2)]
    keys2 = [napis2[i] for i in range(0,len(napis2),2)]

    keys = keys1 + keys2
    keys = list(set(keys))
    keys.sort()

    matrix = { j :{i : 0 for i in keys} for j in keys}

    for i in range(1, len(napis1),2):
        matrix[napis1[i-1]][napis1[i+1]] = int(napis1[i])
        matrix[napis1[i+1]][napis1[i-1]] = int(napis1[i])

    for i in range(1, len(napis2),2):
        matrix[napis2[i-1]][napis2[i+1]] = int(napis2[i])
        matrix[napis2[i+1]][napis2[i-1]] = int(napis2[i])

    znaleziono = []
    chodzenie(napis1[0],keys,matrix,napis2[0],0,znaleziono)
    
    #plot(keys, matrix)

    return min(znaleziono)


print(    
kosp("D3E5J8","H3I2E4J6"),
kosp("A3T5U6","B4G1Y4")	
)
