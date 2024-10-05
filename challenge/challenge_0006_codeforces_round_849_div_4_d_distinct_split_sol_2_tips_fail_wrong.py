# If you feel your problem is hard
# Think your problem the brute-force way first
# Check O(n)
# Think another way to keep your solution under O(n)
#
# Solve something that looks complicated 
# by making simpler steps while keeping the O(n) restriction
# (the lesson I got from ICPC 2023 solving K)
#
# Plus, debug is must by using basic examples
# Plus, think edge cases more
#
# Debug each step
#
# Think start and end point
#
# Keep past data structure until you finish solving

def get_diff_num(s:str):
    alph = [0] * 26
    for character in s:
        if alph[ord(character)-97]==0:
            alph[ord(character)-97]=1
    return sum(alph)

t = int(input())

for test_case in range(t):
    n = int(input())
    s = input()
    diff_nums_acc = []
    
    for index in range(n):
        diff_nums_acc.append(get_diff_num(s[:index+1]))
        
    # debug
    print(diff_nums_acc)
    
    length = 1
    change_point_and_length = []
    change_point = 0
    for i in range(1, n):
        if diff_nums_acc[i-1]==diff_nums_acc[i]:
            length += 1
            # debug: Think all the situation a for loop ends
            if i == (n-1):
                        bar_distinct_num = 1
                        if length > 1:
                            bar_distinct_num = get_diff_num(
                                s[change_point:change_point+length])
                        change_point_and_length.append(
                            (change_point, length, bar_distinct_num))
        else:
            
            # debug
            # print(i)
            
            bar_distinct_num = 1
            if length > 1:
                bar_distinct_num = get_diff_num(
                        s[change_point:change_point+length])
            change_point_and_length.append(
                    (change_point, length, bar_distinct_num))
            length =  1
            change_point = i
        
        # debug
        # print(length)
        # print(change_point)
        
    # debug
    print(change_point_and_length)
    
    max_bar_distinct_num_point = 0
    max_bar_distinct_num = 1
    for bar in change_point_and_length:
        if bar[2] > max_bar_distinct_num:
            max_bar_distinct_num_point = bar[0]
            max_bar_distinct_num = bar[2]
    
    max_length_change_point = 0
    max_length = 1
    for bar in change_point_and_length:
        if bar[1] > max_length:
            max_length_change_point = bar[0]
            max_length = bar[1]
    
    # debug
    print(max_bar_distinct_num_point)
    print(max_bar_distinct_num)
    print(max_length_change_point)
    print(max_length)
    
    if max_bar_distinct_num > 1:
        # debug: should include max_bar_distinct_num_point
        print(get_diff_num(s[:max_bar_distinct_num_point+1])
              +get_diff_num(s[max_bar_distinct_num_point+1:]))
    else: # by max_lengthm, if max_bar_distinct_num == 1
        print(get_diff_num(s[:max_length_change_point+1])
              +get_diff_num(s[max_length_change_point+1:]))
