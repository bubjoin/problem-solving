# Python3 timeout
# PyPy3 OK
import copy
import sys
input = sys.stdin.readline

N = int(input().strip())

claps = [0] * (N + 1) # use index 1 to N except 0

for i in range(1, N + 1):
    num = copy.deepcopy(i)
    while num > 0:
        quotient = num // 10
        remainder = num % 10
        if (remainder!=0) and \
            ((remainder%3==0) or (remainder%6==0) or (remainder%9==0)):
            claps[i] += 1
        num = quotient

print(sum(claps))
