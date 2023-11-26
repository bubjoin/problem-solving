t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    min_index = 0
    for j in range(1, n):
        if arr[min_index] > arr[j]:
            min_index = j
    
    arr[min_index] += 1
    
    product = arr[0]
    
    for j in range(1, n):
        product *= arr[j]
    
    print(product)
    