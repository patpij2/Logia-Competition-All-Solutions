def szyfr(tab,n):
    alfabet = [chr(i) for i in range(97,97+26)] + [' ']
    napis = ' '.join(tab)
    wyniki = []

    for znak in napis:
        if alfabet.index(znak) + n >= len(alfabet):
            ktorynr = abs( n- ( abs( len(alfabet) - alfabet.index(znak) ) ) )
            wyniki.append( alfabet[ktorynr] )

        else:
            ktorynr = alfabet.index(znak) + n
            wyniki.append( alfabet[ktorynr] )

    if wyniki[0] == ' ':
        wyniki.pop(0)
        
    if wyniki[-1] == ' ':
        wyniki.pop(-1)
        
    return ''.join(wyniki)
            
print(
szyfr(['zuzia', 'je' , 'szczaw'],1),
szyfr(['hokus', 'pokus', 'abrakadabra'],26)
)
