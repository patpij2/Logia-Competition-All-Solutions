def czybartka(slowo):
    licznik = 0
    
    for i in slowo:
        if i == 'a':
            licznik += 1
        elif i == 'b':
            licznik -= 1

        if licznik < 0:
            return False
    
    if licznik !=0:
        return False
    return True

def spr(slowo):

    for i in range(len(slowo),-1,-1):
        print(slowo[:i])
        if czybartka(slowo[:i]):
            return i
