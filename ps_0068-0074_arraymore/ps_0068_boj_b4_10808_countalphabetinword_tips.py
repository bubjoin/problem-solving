# a b c d ... z
# 97 98 99 100 ... 122
# 0 1 2 3 4 ... 25

s = input().lower()
s_len = len(s)

# array index matches alphabet
alpha_counter = [0 for i in range(26)]

# for each letter
# check which alphabet it is and increase the count for the alphabet
for i in range(s_len):
    for j in range(26):
        if s[i] == chr(j+97):
            alpha_counter[j] += 1

for i in range(26):
    print(alpha_counter[i], end=" ")