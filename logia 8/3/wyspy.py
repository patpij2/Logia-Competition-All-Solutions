def dt(trasa):
    tab = [[0,28,85,88],[28,0,58,61],[85,58,0,68],[88,61,68,0]]
    suma = 0
    
    for i in range(len(trasa)-1):
        if trasa[i] == 'Tenerife':
            k = 0
        elif trasa[i] == 'La Gomera':
            k = 1
        elif trasa[i] == 'La Palma':
            k = 2
        elif trasa[i] == 'El Hierro':
            k = 3
            
        if trasa[i+1] == 'Tenerife':
            l = 0
        elif trasa[i+1] == 'La Gomera':
            l = 1
        elif trasa[i+1] == 'La Palma':
            l = 2
        elif trasa[i+1] == 'El Hierro':
            l = 3

        suma += tab[k][l]

    return suma

print(
dt([]),
dt(['Tenerife', 'La Gomera', 'El Hierro', 'La Palma', 'Tenerife'])
)

        
