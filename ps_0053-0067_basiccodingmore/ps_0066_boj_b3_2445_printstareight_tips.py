# n 5
# line (n*2-1) == 9

# i 1 2 3 4 5 6 7 8 9
# m       (1+9)/2
# s 1 2 3 4 5 4 3 2 1
# b 8 6 4 2 0 2 4 6 8
# s 1 2 3 4 5 4 3 2 1

n = int(input())
line = n * 2 - 1

m = int((1 + line) / 2) # Python divide makes float, change it to int

# until the middle
for i in range(1, m+1):
    s = i
    b = (m * 2) - (2 * i)
    for j in range(s):
        print("*", end="")
    for j in range(b):
        print(" ", end="")
    for j in range(s):
        print("*", end="")
    print()

# after the middle
for i in range(1, (line-m)+1):
    s = (line-m) - (i-1)
    b = i * 2
    for j in range(s):
        print("*", end="")
    for j in range(b):
        print(" ", end="")
    for j in range(s):
        print("*", end="")
    print()