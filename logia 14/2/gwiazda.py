def kosp(os1,os2):
    wyniki = []
    os1 += 'C'
    os2 += 'C'

    for i in range(0,len(os1),2):
        if os1[i] in os2:
            suma = 0
            for j1 in range(1, i,2):
                suma += int(os1[j1])
                
            for j2 in range(1, os2.index(os1[i]),2):
                suma += int(os2[j2])
            
            wyniki.append(suma)

    '''suma = 0
    for j1 in range(1, len(os1),2):
        suma += int(os1[j1])
            
    for j2 in range(1, len(os2),2):
        suma += int(os2[j2])

    wyniki.append(suma)'''
    
    return min(wyniki)

print(
kosp("D3E5J8","H3I2E4J6"),
kosp("A3T5U6","B4G1Y4")	
)
