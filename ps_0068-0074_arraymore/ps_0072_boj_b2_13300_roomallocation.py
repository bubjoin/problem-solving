import sys
n, k = map(int, sys.stdin.readline().split())

students = [[0, 0] for i in range(6)]

for i in range(n):
    s, g = map(int, sys.stdin.readline().split())
    students[g-1][s] += 1

rooms = 0

for i in range(6):
    for j in range(2):
        if students[i][j]==0:
            continue
        else:
            rooms += (students[i][j] - 1) // k + 1

print(rooms)