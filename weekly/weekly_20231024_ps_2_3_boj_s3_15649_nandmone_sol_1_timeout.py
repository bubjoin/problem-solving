# 1 <= M, N <= 8
# print result on dictionary order

# O(n)
# 80_000_000 * 8 -> FAIL!

N, M = map(int, input().split())

matrix = []

numbers = [ i+1 for i in range(N) ]
numbers_dict = {}
for number in numbers:
    numbers_dict[number]=0

m_size_permutation = [0] * M

# print(numbers)

max_str = ''
min_str = ''

for i in range(M):
    min_str += str(numbers[i])

min = int(min_str)

for i in range(M):
    max_str += str(numbers[N-1-i])

max = int(max_str)

# print(max)
# print(min)

for num in range(min, max+1):
    out = False
    for key in numbers_dict:
        numbers_dict[key]=0
    num_str = str(num)
    for n in num_str:
        if int(n) not in numbers_dict:
            out = True
            break
    if out:
        continue
    for n in num_str:
        numbers_dict[int(n)] += 1
    for k in numbers_dict:
        if numbers_dict[k] >= 2:
            out = True
            break
    if out:
        continue
    matrix.append(num_str)
    
for permutation in matrix:
    for n in permutation:
        print(n, end=' ')
    print()
