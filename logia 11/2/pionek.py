import numpy as np

def pionek(w, p, c):
    dlwiersza=int(len(p)/w)
    p=[int(v) for v in p]
    p=np.array(p)
    print(p)
    p=p.reshape((w, dlwiersza))

    x=0
    y=0
    akx=0
    aky=0
    xmin=0
    ymin=0
    minkrok=0
    for j in range(w):
        for i in range(dlwiersza):
            if p[j][i]==c:
                print(p[j][i])
                akx=i
                aky=j
            if akx >= x or aky >= y:
                xmin=akx-x
                ymin=aky-y
                akx=x
                aky=y
                print(akx, "  ", aky)
            if xmin+ymin<minkrok:
                minkrok=xmin+ymin
    return minkrok
            

