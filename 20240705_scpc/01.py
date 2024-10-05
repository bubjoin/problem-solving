
Answer = 0
str_len = int(input())
ab_str = list(input())

a_pos = []

for i in range(str_len):
    if ab_str[i] == 'A':
        a_pos.append(i)


a_pos_len = len(a_pos)

for i in range(1, a_pos_len):
    gap = a_pos[i] - a_pos[i-1]
    if gap == 1:
        Answer += 2
    elif gap == 2:
        Answer += 1
    else:
        continue

print(Answer)
