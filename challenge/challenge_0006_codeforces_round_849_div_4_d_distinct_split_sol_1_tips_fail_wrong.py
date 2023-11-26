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
# # Keep past data structure until you finish solving

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
    # print(diff_nums_acc)
    
    length = 1
    change_point_and_length = []
    change_point = 0
    for i in range(1, n):
        if diff_nums_acc[i-1]==diff_nums_acc[i]:
            length += 1
            # debug: Think all the situation a for loop ends
            if i == (n-1):
                        change_point_and_length.append((change_point, length))
        else:
            
            # debug
            # print(i)
            
            change_point_and_length.append((change_point, length))
            length =  1
            change_point = i
        
        # debug
        # print(length)
        # print(change_point)
        
    # debug
    # print(change_point_and_length)
    
    max_length_change_point = 0
    max_length = 1
    for bar in change_point_and_length:
        if bar[1] > max_length:
            max_length_change_point = bar[0]
            max_length = bar[1]
    
    # debug
    # print(max_length_change_point)
    # print(max_length)
    
        # debug: should include max_length_change_point
    print(get_diff_num(s[:max_length_change_point+1])
          +get_diff_num(s[max_length_change_point+1:]))
