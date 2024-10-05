
nums_len = int(input())

nums = list(map(int, input().split()))

nums.sort()


chunk = int(nums_len / 4)

seed = [0, chunk*1, chunk*2, chunk*3]

Answer = 0

for i in range(chunk):
    Answer += abs(nums[seed[3]]-nums[seed[2]])
    Answer += abs(nums[seed[2]]-nums[seed[1]])
    Answer += abs(nums[seed[1]]-nums[seed[0]])
    Answer += abs(nums[seed[0]]-nums[seed[3]])

    seed[0] += 1
    seed[1] += 1
    seed[2] += 1
    seed[3] += 1

print(Answer)
