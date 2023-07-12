# n 5
# line (n*2-1)==9

# i 0 1 2 3 4 5 6 7 8
# m   (end_index)/2
# s 9 7 5 3 1 3 5 7 9
# b 0 1 2 3 4 3 2 1 0

n = int(input())
line = n * 2 - 1

m = int((line-1)/2)

# until the middle
for i in range(m+1):
    s = line - (i*2)
    b = i
    for j in range(b):
        print(" ", end="")
    for j in range(s):
        print("*", end="")
    print()

# after the middle
for i in range((line-1)-m):
    s = (i+1)*2 +1
    b = (m-1) - i
    for j in range(b):
        print(" ", end="")
    for j in range(s):
        print("*", end="")
    print()