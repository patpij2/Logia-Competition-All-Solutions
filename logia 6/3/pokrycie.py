def niepokryte(um):
    licznik = 0

    for i in range(20):
        for j in range(20):
            znaleziono = False

            for v in um:
                if (v[0] <= i < v[2] and v[1] <= j < v[3]):
                    znaleziono = True

            if not znaleziono:
                licznik += 1

    print(licznik)
                    
                    
niepokryte([[10,10,20,20],[0,0,20,10],[8,8,12,12]])
