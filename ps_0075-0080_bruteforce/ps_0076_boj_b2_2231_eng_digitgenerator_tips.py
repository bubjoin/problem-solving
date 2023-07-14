# The English version of this problem has to be fixed
# around the input part
# 'The number of test cases T is given in the first line of the input.'
# (and related part in the output part also)
# It has no T in input
#
# The input in English != in Korean
# Input is <= 100000 in English
# Input is <= 1000000 in Korean 
#
# m <= 1000000
# n = abcde
# m = abcde + a + b + c + d + e + f (... + e, in English version)
# a + b + c + d + e + f <= 54 (45, in English version, cannot pass)

def generate_m(n):
    n_copied = n * 1
    digits = []
    while n_copied > 0:
        remainder = n_copied % 10
        digits.append(remainder)
        n_copied = n_copied // 10
    digitsum = n + sum(digits)
    return digitsum
        
m = int(input())

result = 0
for n in range(m - 54, m):
    m_generated = generate_m(n)
    if m_generated == m:
        result = n
        break

if result == 0:
    print(0)
else:
    print(result)