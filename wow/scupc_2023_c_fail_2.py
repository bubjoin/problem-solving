# awkward


N = int(input())

nums = list(map(int, input().split()))

awkward = 0

nums.sort()

print(nums)


sides_max_gap = 0
sides_max_gap_start_index = 0

for i in range(0, N-2):
    sides_gap = 0
    if (i > 0):
        sides_gap += (nums[i]-nums[i-1])
    if ((i+2) < (N-1)):
        sides_gap += (nums[i+3]-nums[i+2])
    if sides_max_gap < sides_gap:
        sides_max_gap = sides_gap
        sides_max_gap_start_index = i

member3 = nums.pop(sides_max_gap_start_index)
nums.pop(sides_max_gap_start_index)
member1 = nums.pop(sides_max_gap_start_index)
awkward += (member1-member3)

print(nums)

two_team = int((N-3)/2)

for i in range(two_team):
    member1 = nums.pop()
    member2 = nums.pop()
    awkward += (member1-member2)

print(awkward)