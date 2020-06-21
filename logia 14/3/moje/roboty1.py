def spotkanie(r1,r2):
    x1,y1,x2,y2 = 0,0,0,0

    r1 = r1*100
    r2 = r2*100
    
    for i in range(100):
        if r1[i] == 'g':
            x1+=1
        elif r1[i] == 'd':
            x1-=1
        elif r1[i] == 'l':
            y1-=1
        elif r1[i] == 'p':
            y1+=1
            
        if r2[i] == 'g':
            x2+=1
        elif r2[i] == 'd':
            x2-=1
        elif r2[i] == 'l':
            y2-=1
        elif r2[i] == 'p':
            y2+=1

        #print(x1,y1,'    ',x2,y2)

        if (x1,y1) == (x2,y2):
            return i+1

    return 0

print(
spotkanie("pd", "g"),
spotkanie("gp", "pg"),
spotkanie("dg", "ggppddllllllllll")	
)
