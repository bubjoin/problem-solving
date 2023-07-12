import sys
n = int(input())

for i in range(n):
    str_1, str_2 = sys.stdin.readline().split()
    
    alphabet = [0 for i in range(26)]
    
    for c in str_1:
        alphabet[ord(c) - 97] += 1
    
    for c in str_2:
        alphabet[ord(c) - 97] -= 1
    
    zeros = True
    for number in alphabet:
        if number != 0:
            zeros = False
    
    if zeros:
        print("Possible")
    else:
        print("Impossible")