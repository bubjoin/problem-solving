import sys
two_three_digits = list(map(list, sys.stdin.readline().split()))
filips_numbers = []

for i in range(2):
    filips_numbers.append(int(two_three_digits[i][2]) * 100 \
        + int(two_three_digits[i][1]) * 10 + int(two_three_digits[i][0]))

if filips_numbers[0] > filips_numbers[1]:
    print(filips_numbers[0])
else:
    print(filips_numbers[1])