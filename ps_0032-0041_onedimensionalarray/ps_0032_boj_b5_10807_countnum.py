import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
v = int(input())

cnt = 0
for num in arr:
    if num == v:
        cnt += 1

print(cnt)