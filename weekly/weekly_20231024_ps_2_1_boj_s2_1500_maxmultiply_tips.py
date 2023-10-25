# 1 <= K <= 20
# K <= S <= 100

# Make hypothesis:
# distribute evenly
# 8 3 -> 2 2 2 -> 3 3 2

S, K = map(int, input().split())

num = S // K

nums = [ num for i in range(K) ]

S = S - (K * num)

# Now, S < K

for i in range(S):
    nums[i] += 1
    
max_multiply = 1
for i in range(K):
    max_multiply *= nums[i]

print(max_multiply)
