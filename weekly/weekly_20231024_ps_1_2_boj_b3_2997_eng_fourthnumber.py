# -100 < integer < 100
# solution not necessarily unique

integers = list(map(int, input().split()))

integers.sort()
min_diff = min(integers[2]-integers[1], integers[1]-integers[0])

if ((integers[2]-integers[1])==min_diff) and \
    ((integers[1])-integers[0]==min_diff):
        if (integers[0] - min_diff) <= -100:
            answer = integers[2] + min_diff
        elif (integers[2] + min_diff) >= 100:
            answer = integers[0] - min_diff
        else:
            answer = integers[2] + min_diff
else:
    if (integers[2]-integers[1]) > (integers[1]-integers[0]):
        answer = integers[1] + min_diff
    else:
        answer = integers[0] + min_diff

print(answer)