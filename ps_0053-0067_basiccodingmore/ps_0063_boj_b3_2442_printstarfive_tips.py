# Imagine a problem
# Draw it precisely
# Observe and find a math

# n 5
# i 1 2 3 4 5
# s 1 3 5 7 9
# b (9-1)/2 (7-1)/2 (5-1)/2 (3-1)/2 (1-1)/2
# b 4 3 2 1 0

n = int(input())

for i in range(1, n+1):
    s = 1 + (i - 1) * 2
    b = n - i
    for j in range(b):
        print(" ", end="")
    for j in range(s):
        print("*", end="")
    print()