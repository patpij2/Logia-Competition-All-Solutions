def ilep(s):
    licznik=0
    for i in range(len(s)):
        for j in range(i, len(s)+1):
            tab = [i for i in s[i:j]]
            if tab == tab[::-1]:
                if tab:
                    print(tab)
                    licznik+=1
    print(licznik)
