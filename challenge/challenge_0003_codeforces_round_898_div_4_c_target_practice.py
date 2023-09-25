t = int(input())

for test in range(t):
    target = []
    for i in range(10):
        line = list(input())
        target.append(line)
    
    total_score = 0
    
    for y in range(10):
        for x in range(10):
            if target[y][x] == 'X':
                if (y==0) or (y==9) or (x==0) or (x==9):
                    total_score += 1
                elif (y==1) or (y==8) or (x==1) or (x==8):
                    total_score += 2
                elif (y==2) or (y==7) or (x==2) or (x==7):
                    total_score += 3
                elif (y==3) or (y==6) or (x==3) or (x==6):
                    total_score += 4
                else:
                    total_score += 5
    
    print(total_score)