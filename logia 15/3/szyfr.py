def deszyfr(alfa,tab):
    alfa = " " + alfa
    napis = ''.ljust(len(tab),'0')
    napis = [i for i in napis]

    for i in range(len(tab)):
        napis[tab[i][1]//10-1] = alfa[tab[i][0]//10]

    napis = ''.join(napis)

    return napis.split()

print(
deszyfr('rklotam',[[60,10],[30,20],[60,30],[0,40],[70,50],[60,60],[0,70],[20,80],[40,90],[50,100],[60,110]]),
deszyfr('acdeh',[[10,20],[30,10],[50,40],[20,30]])
)
