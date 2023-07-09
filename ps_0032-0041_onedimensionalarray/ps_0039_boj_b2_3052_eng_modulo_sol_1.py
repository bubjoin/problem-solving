arr = []
for i in range(10):
    arr.append(int(input()))

for i in range(10):
    arr[i] = arr[i] % 42

print(len(set(arr)))