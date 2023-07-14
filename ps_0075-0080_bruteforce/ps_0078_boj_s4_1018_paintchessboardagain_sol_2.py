import sys
n, m = map(int, sys.stdin.readline().split())

board = [0 for i in range(m*n)]
for i in range(n):
    line = list(map(str, sys.stdin.readline()))
    for j in range(m):
        if line[j]=='B':
            board[m*i+j] = 1

least_count = 64
bingo = False
for i1 in range(0, n-7):
    for j1 in range(0, m-7):
        count_diff = 0
        for i2 in range(8):
            for j2 in range(8):
                bw = (i2+j2)%2
                if board[(m*i1+j1)+m*i2+j2]!=bw:
                    count_diff += 1
        if count_diff > 32:
            count_diff = 64 - count_diff
        if count_diff < least_count:
            least_count = count_diff
            if least_count == 0:
                bingo = True
        if bingo:
            break
    if bingo:
        break

print(least_count)