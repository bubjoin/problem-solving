# Imagine a problem
# Observe and find a math

import sys

for play in range(3):
    yut = list(map(int, sys.stdin.readline().split()))
    yut = sum(yut)
    if yut == 3:
        print("A")
    elif yut == 2:
        print("B")
    elif yut == 1:
        print("C")
    elif yut == 0:
        print("D")
    else: # yut == 4
        print("E")