t = int(input())

for test_case in range(t):
    n, x = map(int, input().split())
    corals = list(map(int,input().split()))
    
    corals.sort()
    # print(corals)
    
    max_coral = max(corals)
    min_coral = min(corals)
        
    level_waters_acc = [0] 
    bottom = min_coral
    
    for i in range(1, n):
        if bottom < corals[i]:
            level_waters_acc.append(level_waters_acc[-1] + (i * (corals[i]-bottom)))
            bottom = corals[i]
        else:
            level_waters_acc.append(level_waters_acc[-1])
    
    # print(level_waters_acc)
    
    if level_waters_acc[-1] > x :        
        for i in range(n):
            if level_waters_acc[i] > x:
                gap = x - level_waters_acc[i-1]
                diff = gap // i
                h = corals[i-1] + diff
                break        
        print(h)
    else:
        h = max_coral + ((x - level_waters_acc[-1])//n)
        print(h)
        