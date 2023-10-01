t = int(input())

for test_case in range(t):
    n, x = map(int, input().split())
    corals = list(map(int,input().split()))
    
    h = min(corals) + (x//n) # timeout on test1, test10 solved
    while True:        
        waters = []
        for i in range(n):
            if (h - corals[i]) < 0:
                waters.append(0)
            else:
                waters.append(h - corals[i])
        
        sum_waters = sum(waters)
        if (sum_waters == x):
            break
        elif (sum_waters > x):
            h = h - 1
            break
        else:
            diff_h = (x - sum_waters)//n # timeout on test3 solved
            if diff_h > 0:
                h += diff_h
            else:
                h += 1
    print(h)

# timeout on test20