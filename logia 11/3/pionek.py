import numpy as np

def pionek(s):
    x1,y1,z1= 0,0,0
    x2,y2,z2= 0,0,0
    tab = np.array([i for i in s])
    tab = tab.reshape((3,3,3))
    #print(tab)

    for x in range(3):
        for y in range(3):
            for z in range(3):
                if tab[x][y][z] == 'c':
                    x1,y1,z1 = x,y,z
                    break

    for x in range(3):
        for y in range(3):
            for z in range(3):
                if tab[x][y][z] == 'c' and (x,y,z) != (x1,y1,z1):
                    x2,y2,z2 = x,y,z
                    break

    return abs(x2-x1)+abs(y2-y1)+abs(z2-z1)


print(
pionek ("cbbbbbbbbbbbbbbbbbbbbbbbbbc"),
pionek ("bbbbbbbbbbbbbbbbbbbcbbbbbbc")
)
