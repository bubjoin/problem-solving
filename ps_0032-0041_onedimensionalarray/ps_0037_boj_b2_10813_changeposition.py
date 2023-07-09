import sys
n, m = map(int, sys.stdin.readline().split())

# initialize
arr = [(i + 1) for i in range(n)]

for i in range(m):
    i, j = map(int, sys.stdin.readline().split())
    
    # Nth number encoding to index
    i = i - 1
    j = j - 1
    
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

for num in arr:
    print(num, end=" ")