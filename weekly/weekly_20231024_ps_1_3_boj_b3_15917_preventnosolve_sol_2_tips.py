# 1 <= Q <= 1_000_000
# 1 <= a <= 2**31 - 1
# 2**x yes 1, no 0

# timeout solution: 
# If you use input() many times
# you MUST use sys.stdin.readline for input
#
# more:
# sys.stdout.write("string\n"), instead of print("string")
import sys
input = sys.stdin.readline

Q = int(input())

power_list = [1] * 32
for i in range(1, 32):
    power_list[i] = power_list[i-1] * 2

power_dict = {}
for power in power_list:
    power_dict[power]=1

for q in range(Q):
    a = int(input())
    found = power_dict.get(a, 0)
    if found:
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")
