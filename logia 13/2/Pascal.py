def Pascal(w, p):
    if w==1 and p!=1:
        return 0
    if p==1:
        return 1
    else:
        return Pascal(w-1, p-1)+Pascal(w-1, p)
