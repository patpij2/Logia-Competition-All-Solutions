def slowoslawka(slowo,wyroznione):
    for i in range(len(slowo)):
        if slowo[i] == wyroznione[0]:
            if slowo[:i].count(wyroznione[1]) > 0:
                return False
            
            if slowo[:i].count(wyroznione[2]) > 0:
                return False
            
        if slowo[i] == wyroznione[1]:
            if slowo[:i].count(wyroznione[2]) > 0:
                return False
            
            if slowo[i+1:].count(wyroznione[0]) > 0:
                return False

        if slowo[i] == wyroznione[2]:
            if slowo[i+1:].count(wyroznione[0]) > 0:
                return False
            
            if slowo[i+1:].count(wyroznione[1]) > 0:
                return False

    if slowo.count(wyroznione[0]) == 0:
        return False
    if slowo.count(wyroznione[1]) == 0:
        return False
    if slowo.count(wyroznione[2]) == 0:
        return False

    return True

def usuwanie(i,wyniki,slowo,wyroznione):
    if i==0:
        if slowoslawka(slowo,wyroznione):
            if slowo not in wyniki :
                wyniki.append(slowo)
            
    else:
        for j in range(len(slowo)):
            usuwanie(i-1,wyniki,slowo[:j]+slowo[j+1:],wyroznione)
            
def abc(slowo,wyroznione,nr):
    wyniki = []

    for i in range(len(slowo)):
        usuwanie(i,wyniki,slowo,wyroznione)

    wyniki.sort()
    return wyniki[nr-1]

print(
abc('abebc','abc',5)
)
