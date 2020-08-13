def litera(tab):
    tab = ''.join(tab)
    maks = max([tab.count(i) for i in tab])
    teraz_wyniki = [i for i in tab if tab.count(i) == maks]
    bez_powtorzen = [i for i in set(teraz_wyniki)]
    bez_powtorzen.sort()

    print(bez_powtorzen)
    
      
litera(['ala','ma','kota'])
litera(['julka','lubi','psy'])
