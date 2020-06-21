def spotkanie(r1, r2):
    robot1,robot2 = [0,0],[0,0]

    for i in range(100):
        if r1[i%len(r1)] == 'l':
            robot1[0] -=1
        if r1[i%len(r1)] == 'p':
            robot1[0] +=1
        if r1[i%len(r1)] == 'g':
            robot1[1] +=1
        if r1[i%len(r1)] == 'd':
            robot1[1] -=1

        if r2[i%len(r2)] == 'l':
            robot2[0] -=1
        if r2[i%len(r2)] == 'p':
            robot2[0] +=1
        if r2[i%len(r2)] == 'g':
            robot2[1] +=1
        if r2[i%len(r2)] == 'd':
            robot2[1] -=1

        #print(robot1, '     ' ,robot2)
        if robot1 == robot2:
            return i+1
    return 0

print(
spotkanie("pd", "g"),
spotkanie("gp", "pg"),
spotkanie("dg", "ggppddll")
)
