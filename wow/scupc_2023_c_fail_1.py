# awkward


N = int(input())

nums = list(map(int, input().split()))

awkward = 0

nums.sort()

# print(nums)


min_three = 500000
min_three_start = 500000
for i in range(0, N-2):
     if (nums[i+2] - nums[i]) < min_three:
         min_three = nums[i+2] - nums[i]
         min_three_start = i

member3 = nums.pop(min_three_start)
nums.pop(min_three_start)
member1 = nums.pop(min_three_start)
awkward += (member1-member3)

# print(nums)


two_team = int((N-3)/2)

for i in range(two_team):
    member1 = nums.pop()
    member2 = nums.pop()
    awkward += (member1-member2)

print(awkward)