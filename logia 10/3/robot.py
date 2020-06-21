def robot(trasa):
    x,y = 0,0
    kroki = [[0,0,0,0]]
    kroki2 = []
    wyniki = []

    for kier in trasa:

        if kier == 'N':
            y += 1

        elif kier == 'S':
            y -= 1

        elif kier == 'E':
            x += 1

        elif kier == 'W':
            x -= 1

        kroki.append([kroki[-1][2],kroki[-1][3],x,y])

    kroki.pop(0)

    for krok in kroki:
        kroki2.append([krok[2],krok[3],krok[0],krok[1]])

    kroki.extend(kroki2)

    for i in kroki:
        if not i in wyniki:
            wyniki.append(i)

    return ((len(trasa) - len(wyniki)//2 ))

print(
robot('NESW'),
robot('NNNESSSSWNNNE'),
robot('NESWNESW')
)

