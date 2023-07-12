# Find hidden conditions in problem
# Think which is not given
# Consider all possible cases in a stage

import sys
a, b = map(int, sys.stdin.readline().split())

# because not given which one is bigger
if a > b:
    a, b = b, a

count_strictly_between = b - a - 1

if count_strictly_between==0:
    print(count_strictly_between)
elif count_strictly_between==-1: # if a, b are the same numbers
    print(0)
else:
    print(count_strictly_between)
    for n in range(a + 1, b):
        print(n, end=" ")