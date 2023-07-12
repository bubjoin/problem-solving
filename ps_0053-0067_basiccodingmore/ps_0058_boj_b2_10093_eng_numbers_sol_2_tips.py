# Numbers strictly between a and b
# how to deal with 1 <= a, b <= 1,000,000,000,000,000
# converting number string to array

# When you write a block, think every possible situation
# Test all possible cases right after writing each block

# When you debug, think every possible input situation
# Think about edge case and corner case
# Always think in terms of data
# Test each input situation, validate the result of it
# Divide a process and think of a small part of it
# Choose a period and print its log between the start, end, middle of it
# Narrow the period, and do it again
# Take a walk, have a snack, take a rest, and try finding the error part again

# Take a rest

# Think small, even when you write a code

# Must remember some method has no return
# a = zeros.extend(a).copy() doesn't work

# Think about another version
# using arrays, * 10, % 10, // 10, and loops

import sys

def get_bigger(a:list, b:list) -> list:
    for i in range(len(a)):
        if (a[i] != 0) or (b[i] != 0):
            if a[i] > b[i]:
                return a
            elif a[i] < b[i]:
                return b
            else: # a[i] == b[i]:
                continue
    return b        
                    
def get_gap(a:list, b:list) -> int:
    # make b > a
    if get_bigger(a, b) is a:
        a, b = b, a
    
    # get (b - a) array
    b_minus_a = b.copy() # make a copy
    for i in range(15, -1, -1):
        if b_minus_a[i] < a[i]:
            b_minus_a[i-1] -= 1
            b_minus_a[i] = 10 + b_minus_a[i] - a[i]
        else:
            b_minus_a[i] = b_minus_a[i] - a[i]
    
    # check if all zeros
    all_zeros = True
    for i in range(len(b_minus_a)):
        if b_minus_a[i]!=0:
            all_zeros = False
            break
            
    # if all zeros
    if all_zeros:
        return 0
    
    # or
    else:
        # get (b - a) string
        b_minus_a_to_string = ""
        first_non_zero_index = 0
        for i in range(len(b_minus_a)):
            if b_minus_a[i]!=0:
                first_non_zero_index = i
                break
        for i in range(first_non_zero_index, len(b_minus_a)):
            b_minus_a_to_string += str(b_minus_a[i])
        
        # convert the string to integer
        # return ((b - a) - 1)
        count_strictly_between = int(b_minus_a_to_string)- 1
        return count_strictly_between
        
def get_next_number(a:list) -> list:
    # check if all zeros
    all_zeros = True
    for n in a:
        if n != 0:
            all_zeros = False
            break
    
    # if all zeros
    if all_zeros:
        next_number = [0 for i in range(len(a))]
        next_number[-1] = 1
        return next_number
    
    # or
    else:
        # make a copy
        next_number = a.copy()
        # number + 1
        up = 0
        for i in range((len(a) - 1), -1, -1):
            if i == (len(a) - 1):
                if (a[i] + 1) == 10:
                    next_number[i] = 0
                    up = 1
                else:
                    next_number[i] += 1
                    return next_number
            else:
                if (a[i] + up) == 10:
                    next_number[i] = 0
                    up = 1
                else:
                    next_number[i] += up
                    return next_number                  

# main
a, b = map(list, sys.stdin.readline().split())
a = list(map(int, a))
b = list(map(int, b))

# Must remember some method has no return
# a = zeros.extend(a).copy() doesn't work
zeros = 16 - len(a)
zeros = [0 for i in range(zeros)]
zeros.extend(a)
a = zeros.copy()
zeros = 16 - len(b)
zeros = [0 for i in range(zeros)]
zeros.extend(b)
b = zeros.copy()

starting_number = a
if get_bigger(a, b) is a:
    starting_number = b

count_strictly_between = get_gap(a, b)

if count_strictly_between == 0:
    print(count_strictly_between)
else:
    print(count_strictly_between)
    for i in range(count_strictly_between):
        next_number = get_next_number(starting_number)
        starting_number = next_number
        first_no_zero = False
        for j in range(len(next_number)):
            if next_number[j] == 0:
                if first_no_zero == False:
                    print("", end="")
                else:
                    print(next_number[j], end="")
            else:
                first_no_zero = True
                print(next_number[j], end="")
        print(" ", end="")