import sys
n, m = map(int, sys.stdin.readline().split())
arr = [0 for i in range(n)]

for m in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    
    # Nth number encoding to index
    i = i - 1
    j = j - 1
    
    for idx in range(i, j + 1):
        arr[idx] = k
    
for num in arr:
    print(num, end=" ")