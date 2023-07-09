import sys
n, m = map(int, sys.stdin.readline().split())

baskets = [i + 1 for i in range(n)]

for i in range(m):
    i, j = map(int, sys.stdin.readline().split())
    
    i = i - 1
    j = j - 1
    
    # think about what condition ends the loop
    # in the both cases that the length of the array is odd/even
    while i < j: 
        temp = baskets[i]
        baskets[i] = baskets[j]
        baskets[j] = temp
        i += 1
        j -= 1

for basket_num in baskets:
    print(basket_num, end=" ")