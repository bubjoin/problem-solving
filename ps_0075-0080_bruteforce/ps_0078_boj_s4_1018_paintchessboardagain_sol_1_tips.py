import sys
n, m = map(int, sys.stdin.readline().split())
board = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    line = list(map(str, sys.stdin.readline()))
    line.pop() # pop the last '\n'
    for j in range(m):
        if line[j]=='B':
            board[i][j] = 1

model = [[[((i+j)%2) for j in range(8)] for i in range(8)], \
         [[((i+j)+1)%2 for j in range(8)] for i in range(8)]]

least_count = 64
for i in range(0, n-7):
    for j in range(0, m-7):
        # cut 8x8 board not using numpy, using zip and unpack
        board_cut = [board[i2] for i2 in range(i, i+8)]
        board_cut = list(zip(*(list(zip(*board_cut))[j:j+8])))
        
        for k in range(2):
            count_diff = 0
            for i2 in range(8):
                for j2 in range(8):
                    if board_cut[i2][j2]!=model[k][i2][j2]:
                        count_diff += 1
            if count_diff < least_count:
                least_count = count_diff

print(least_count)