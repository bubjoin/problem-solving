# Find an appropriate data structure to apply after reading a problem

# Using data as index

arr = [0 for i in range(1000)] # data 0-999 to index 0-999

for i in range(10):
    num = int(input())
    num = num % 42
    arr[num] = 1

cnt_distinct = 0

for distinct in arr:
    if distinct == 1:
        cnt_distinct += 1
        
print(cnt_distinct)