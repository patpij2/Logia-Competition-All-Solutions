from turtle import *
import numpy as np

def sprawdz(h,s):
    iw=int(len(s)/h)
    licznik=0
    maks=-1000000

    for i in range(iw):
        licznik=0
        for j in range(h):
            if s[j]==s[j+1] and s[j]=='1':
                licznik+=1
            else:
                if licznik>maks:
                    maks=licznik
    return licznik

def wzorek(h,s):
    pass
