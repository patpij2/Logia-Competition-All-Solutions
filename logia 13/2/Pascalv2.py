def Pascal(w, p):
    wiersz=[1,0]
    for i in range(2, w+1):
        nowywiersz=[1]
        for j in range(i-1):
            nowywiersz.append(wiersz[j]+wiersz[j+1])
        nowywiersz.append(0)
        wiersz=nowywiersz.copy()
    return wiersz[p-1]
