# n 5
# i 1 2 3 4 5
# s 9 7 5 3 1
# s 5*2-1 4*2-1 3*2-1 2*2-1 1*2-1
# b 0 1 2 3 4
# b 1-1 2-1 3-1 4-1 5-1

n = int(input())
for i in range(1, n+1):
    s = (n - (i - 1)) * 2 - 1
    b = i - 1
    for j in range(b):
        print(" ", end="")
    for j in range(s):
        print("*", end="")
    print()