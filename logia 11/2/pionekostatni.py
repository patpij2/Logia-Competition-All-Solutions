import numpy as np

def pionek(w, p, c):
    k=int(len(p)/w)
    tab = np.array([int(i) for i in p])
    tab= tab.reshape((w,k))
    print(tab)
    odleglosci=[]
    
    for y1 in range(k):
        for x1 in range(w):
            for y2 in range(k):
                for x2 in range(w):
                    if tab[x1][y1]==tab[x2][y2] and tab[x1][y1]==c and (x1, y1) != (x2, y2):
                        odleglosci.append(abs(x2-x1)+abs(y2-y1))
    print('odleglosci: ', odleglosci)
    
    return min(odleglosci)
                        
    
    


#print (pionek(3, "532378832375", 5))
print (pionek(2, "444474744474", 7))
