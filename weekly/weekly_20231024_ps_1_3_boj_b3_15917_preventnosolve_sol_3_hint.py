# hint:
# If a is 2**x
# (a&(-a))==a yes 1 no 0

# timeout solution: 
# If you use input() many times
# you MUST use sys.stdin.readline for input
import sys
input = sys.stdin.readline

Q = int(input())

for q in range(Q):
    a = int(input())
    if (a&(-a))==a:
        print(1)
    else:
        print(0)
