def perm(tab,k):
    wyniki = []
    if k == 0:
        wyniki.append(tab.copy())
    else:
        for i in range(k):
            tab[i],tab[k-1] = tab[k-1],tab[i]
            wyniki.extend( perm(tab,k-1) )
            tab[i],tab[k-1] = tab[k-1],tab[i]
    return wyniki

def rating(tab1,tab2):
    diffs = 0
    for i in range(len(tab1)):
        if tab1[i] != tab2[i]:
            diffs += 1

    for i in range(len(tab1)):
        for j in range(len(tab1)):
            if i != j:
                if tab1[i] == tab2[j] and tab1[j] == tab2[i]:
                    diffs-=0.5

    if diffs >2:
        diffs -=1
    return int(diffs)
            

def miasta(a,t,z):
    perms = perm([i for i in a],len(a))
    grades = []

    for p in perms:
        grade = rating(p,[i for i in a]) + rating(p,[i for i in t]) + rating(p,[i for i in z])
        grades.append(grade)

    
    return print(perms[grades.index(min(grades))]
