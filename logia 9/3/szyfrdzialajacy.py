def szyfr(slowa):
    wyniki = []
    for slowo in slowa:

        while int(len(slowo)**0.5) != len(slowo)**0.5:
            slowo = slowo+' '
        
        tab = [[ slowo[0] ]]

        i=1
        n=0
        while i < len(slowo):
            if n%2 == 0:
                tmp = []
                for j in range(len(tab)):
                    tmp.append(slowo[i])
                    i+=1
                tab.insert(0,tmp)

                for j in range(len(tab)):
                    tab[j].append(slowo[i])
                    i+=1
                n+=1
            else:
                tmp = []
                for j in range(len(tab)):
                    tmp.insert(0,slowo[i])
                    i+=1
                tab.append(tmp)

                for j in range(len(tab)-1,-1,-1):
                    tab[j].insert(0,slowo[i])
                    i+=1
                n+=1
        tmp_slowo = ''
        for i in tab:
            for j in i:
                if j != ' ':
                    tmp_slowo += j
        wyniki.append(tmp_slowo)
            
    return wyniki

print(                
szyfr(['abc','defg','hijkl']),
szyfr(["konkurs","logia"])
)
