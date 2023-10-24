# 1 <= Q <= 1_000_000
# 1 <= a <= 2**31 - 1
# 2**x yes 1, no 0

# timeout solution: 
# If you use input() many times
# you MUST use sys.stdin.readline for input
import sys
input = sys.stdin.readline

Q = int(input())

# power_list = [2**i for i in range(32)]

power_list = [1] * 32
for i in range(1, 32):
    power_list[i] = power_list[i-1] * 2

for q in range(Q):
    a = int(input())
    yes = False
    for power in power_list:
        if power==a:
            yes = True
            break
    if yes:
        print(1)
    else:
        print(0)
