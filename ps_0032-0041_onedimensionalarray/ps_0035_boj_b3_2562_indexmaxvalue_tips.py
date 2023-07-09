arr = []
for i in range(9):
    arr.append(int(input()))
    
max_idx = 0

for i in range(9):
    if arr[i] > arr[max_idx]:
        max_idx = i

print(arr[max_idx])
print(max_idx + 1) # the answer is (max_idx + 1)th number