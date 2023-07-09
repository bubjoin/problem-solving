arr = [0 for i in range(30)]

for i in range(28):
    num = int(input())
    num = num - 1
    arr[num] = 1
    
for idx in range(30):
    if arr[idx] == 0:
        num = idx + 1
        print(num)