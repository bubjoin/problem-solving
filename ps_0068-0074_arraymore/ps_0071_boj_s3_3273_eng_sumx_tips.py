# You can put a source into a function and printing out the return
# instead of just executing the source and printing the result
# Some platforms require writing an answer in a function

def sumx():
    import sys
    n = int(input())
    a_set = list(map(int, sys.stdin.readline().split()))
    x = int(input())

    count_pairs = 0

    i = 0
    j = n - 1

    a_set.sort()

    while i < j:
        if (a_set[i] + a_set[j]) == x:
            count_pairs += 1
            i = i + 1
            j = j - 1
        elif (a_set[i] + a_set[j]) > x:
            j = j - 1
        else: # (a_set[i] + a_set[j]) < x
            i = i + 1
    
    return count_pairs

print(sumx())        