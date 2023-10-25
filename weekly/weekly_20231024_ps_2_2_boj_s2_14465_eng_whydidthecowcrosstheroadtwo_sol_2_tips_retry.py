# Read problem carefully

# Comment titles to code blocks, for debugging
# Make the title look different to find easily
# or make enough room between the code blocks

# <Problem>
# 1 <= B, K <= N <= 100_000
# get minimum number of signals to be repaired to make continuous block of K

# <example>
# 10 6 5
# 2\n10\n1\n5\n9
# 0 0 1 1 0 1 1 1 0 0
# 0 broken 1 ok
# 1 1 1 1 1 1
# 1

# <Logic>
# You can repair 0 -> 1
# but can't make things broken

# ok bar length <= K
# (k-ok bar + ok bar) left side one should be broken or wall
# or 
# (ok bar + k-ok bar) right side one should be broken or wall

# don't forget the road size
# k bar should be in the road

# when it satisfy above conditions
# save the number of brokens in k block

# choose minimal one

# check O(n) for each step

# Don't forget the case all broken
# Don't forget the case N == 1

N, K, B = map(int, input().split())

brokens = []
for i in range(B):
    brokens.append(int(input()))

crosswalks = [1] * N

for broken in brokens:
    crosswalks[broken-1]=0

# Get ok bars (start, end) list
ok_bars =[]

start = None
end = None
for i in range(N):
    if (crosswalks[i]==1) and (start is None):
        start = i
        if (i == N-1):
            end = i
            ok_bars.append((start,end))
            break
        elif (crosswalks[i+1]==0):
            end = i
            ok_bars.append((start,end))
            start = None
            end = None
            continue
        else:
            continue
    elif crosswalks[i]==1:
        if (i == N-1):
            end = i
            ok_bars.append((start,end))
            break
        elif (crosswalks[i+1]==0):
            end = i
            ok_bars.append((start,end))
            start = None
            end = None
            continue
        else:
            continue
    else: # crosswalks[i]==0
        pass

# print(ok_bars)


# Find repair nums
repair_nums = []

def get_broken_num(start, end):
    zeros = 0
    for i in range(start, end+1):
        if crosswalks[i] == 0:
            zeros += 1
    return zeros

for ok_bar in ok_bars:
    bar_length = ok_bar[1] - ok_bar[0] + 1
    if bar_length==K:
        repair_nums.append(0)
        break
    elif bar_length < K:
        rest = K - bar_length
        k_start = ok_bar[0] - rest
        if k_start >= 0:
            repair_nums.append(get_broken_num(k_start, ok_bar[1]))
        
        k_end = ok_bar[1] + rest
        if k_end <= (N-1):
            repair_nums.append(get_broken_num(ok_bar[0], k_end))
    else: # bar_length > K
        pass

# If no ok block
# repair num is K
if len(ok_bars)==0:
    repair_nums.append(K)

# print(repair_nums)

# Find minimal repair num
repair_nums.sort()
print(repair_nums[0])
