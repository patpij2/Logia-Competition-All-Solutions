from turtle import *

def kwd(a,k):
    if k:
        fillcolor('green')
        begin_fill()
    for i in range(4):
        fd(a); rt(90)
    fd(a)
    if k:    
        end_fill()

def szyfruj(n):
    napis=[v for v in n]
    tab=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    znak=0
    for j in napis:
        znak= tab.index(j)  
        print(znak)
    '''
    do5=0
    for i in len(tab):
        
        do5+=1
        if do5==5:
            
    
    lt(90)
'''
