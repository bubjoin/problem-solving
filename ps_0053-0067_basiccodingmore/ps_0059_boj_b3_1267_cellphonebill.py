import sys

n = int(input())

time_list = list(map(int, sys.stdin.readline().split()))

y = 0
m = 0

for time in time_list:
    
    # y //30 q0 won10  30 1 20  30 2 30  30 3 40
    y += ((time // 30) + 1) * 10
    # m //60 q0 won15  60 1 30  60 2 45  60 3 60
    m += ((time // 60) + 1) * 15

if y == m:
    print(f"Y M {y}")
elif y < m:
    print(f"Y {y}")
else: # m < y
    print(f"M {m}")