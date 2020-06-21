def palindrom(s):
    for i in range(len(s)):
        if s[i]!=s[-i-1]:
            return False
    return True
            
def ilep(s):
    licznik=0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if palindrom(s[i:j+1]):
                licznik+=1
    return licznik

                
