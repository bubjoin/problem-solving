# Python3 OK
# Divide when no common pattern
# Bind things that have common pattern

import sys
input = sys.stdin.readline

# N <= 1_000_000

N = int(input().strip())

claps = [0] * (N + 1) # index 1 to N except 0 for a number

for gap in [10, 100, 1_000, 10_000, 100_000, 1_000_000]:
    for i in range(3*(gap//10), N + 1, gap):
        for j in range(gap//10):
            if (i + j) < (N + 1):
                claps[i+j] += 1
    for i in range(6*(gap//10), N + 1, gap):
        for j in range(gap//10):
            if (i + j) < (N + 1):
                claps[i+j] += 1
    for i in range(9*(gap//10), N + 1, gap):
        for j in range(gap//10):
            if (i + j) < (N + 1):
                claps[i+j] += 1

# For debugging
# print([(i%10) for i in range(N+1)])
# print(claps)

print(sum(claps))