import numpy as np

def pionek(w, p, c):
    ik=int(len(p)/w)
    tab = np.array( [int(i) for i in p] )
    tab = tab.reshape((w, ik))
    #print(tab)

    wyniki = []
    
    for y1 in range(w):
        for x1 in range(ik):
            for y2 in range(w):
                for x2 in range(ik):
                    if tab[y1][x1]==tab[y2][x2]==c and (x1,y1)!=(x2,y2):
                        wyniki.append(abs(abs(x1-x2)+abs(y1-y2)))
                        
                        

    print(min(wyniki))

pionek(1, "444474744474", 7)
pionek(2, "444474744474", 7)
pionek(3, "532378832375", 5)
