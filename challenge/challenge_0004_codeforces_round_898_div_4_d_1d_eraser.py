t = int(input())

for test_case in range(t):
    n, k = map(int, input().split())
    s = list(input())
    black_indexs = []
    for i in range(len(s)):
        if s[i]=='B':
            black_indexs.append(i)
    
    if (len(black_indexs)==0):
        print(0)
    else:
        pos_eraser_start = black_indexs[0]
        count_eraser = 1
        for index in black_indexs[1:]:
            if (pos_eraser_start -1 + k) >= index:
                continue
            else:
                pos_eraser_start = index
                count_eraser += 1
        print(count_eraser)