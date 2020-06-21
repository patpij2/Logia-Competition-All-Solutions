def poler(droga):
    xy_tab = [[0,0]]
    yx_tab = [[0,0]]
    x,y = 0,0
    
    for i in droga:
        if i == 'g':
            y+=1
        elif i == 'd':
            y-=1
        elif i == 'p':
            x+=1
        elif i == 'l':
            x-=1

        xy_tab.append([x,y])
        yx_tab.append([y,x])

    xymin = min(xy_tab)
    xymax = max(xy_tab)
    yxmin = min(yx_tab)[::-1]
    yxmax = max(yx_tab)[::-1]

    x_dl = max(abs(xymin[0]) + abs(xymax[0]), abs(xymin[1]) + abs(xymax[1]))
    y_dl = max(abs(yxmin[0]) + abs(yxmax[0]), abs(yxmin[1]) + abs(yxmax[1]))

    print(x_dl,y_dl)
    
    
poler("lllgpdddd")
