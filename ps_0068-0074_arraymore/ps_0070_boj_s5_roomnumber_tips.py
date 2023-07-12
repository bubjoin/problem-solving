# Divide the problem to the extent that
# You feel comfortable with the size of the code to deal with

# numbers needed
# digit_count_array
# 0 1 2 3 4 5 6 7 8 9
# 2 3 4 5 2 3 4 2 3 4
#
# most_needed == set_needed
#
# but, before get most needed
# 6 or 9 needed != 0
# six_or_nine_needed = (6 needed + 9 needed -1) // 2  + 1
#
# most_needed except 6 and 9
#
# compare most_needed vs six_or_nine_needed

n = list(map(int, input()))

digit_count_array = [0 for i in range(10)]

most_needed_index = 0
most_needed = 0
six_or_nine_needed = 0

# count each number 0-9 in input number
for i in range(len(n)):
    for j in range(10):
        if n[i] == j:
            digit_count_array[j] += 1

# six_or_nine_needed
if (digit_count_array[6] + digit_count_array[9]) > 0:
    six_or_nine_needed = ((digit_count_array[6] + digit_count_array[9] - 1) \
        // 2) + 1

# most needed except 6 or 9
for i in range(len(digit_count_array)):
    if (i==6) or (i==9):
        continue
    
    # MUST check initial case
    if digit_count_array[i] > digit_count_array[most_needed_index]:
        most_needed_index = i

most_needed = digit_count_array[most_needed_index]

# find answer and print
if most_needed > six_or_nine_needed:
    set_needed = most_needed
else:
    set_needed = six_or_nine_needed

print(set_needed)