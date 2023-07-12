# n 5
# line n*2-1 == 9

# i 1 2 3 4 5 6 7 8 9
# m      (1 + 9)/2
# s 1 3 5 7 9 7 5 3 1
# b 4 3 2 1 0 1 2 3 4

n = int(input())
line = n * 2 - 1

m = int((1+line)/2)

# until the middle
for i in range(1, m+1):
    s = 1 + (i - 1) * 2
    b = m - i
    for j in range(b):
        print(" ", end="")
    for j in range(s):
        print("*", end="")
    print()

# after the middle
for i in range(1, (line-m)+1):
    b = i
    s = line - i * 2
    for j in range(b):
        print(" ", end="")
    for j in range(s):
        print("*", end="")
    print()