import sys
three_numbers = list(map(int, sys.stdin.readline().split()))

# three_numbers.sort()

# selection sort
for i in range(len(three_numbers)-1):
    for j in range((i + 1), len(three_numbers)):
        if three_numbers[i] > three_numbers[j]:
            temp = three_numbers[i]
            three_numbers[i] = three_numbers[j]
            three_numbers[j] = temp

for num in three_numbers:
    print(num, end=" ")