# Python
# For readability

# 1000000 == 1_000_000
# True
# -1000000 == -1_000_000
# True

# -1000000 == -_1_000_000
# NameError: name '_1_000_000' is not defined

import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

max = arr[0] # in case there is only one element in the array
min = arr[0] # in case there is only one element in the array

for num in arr:
    if num > max:
        max = num
    if num < min:
        min = num

print(min, max, sep=" ")