string = input()
arr_string = list(string)

for i in range(ord('a'), ord('z')+1):
    being = False
    for j in range(len(arr_string)):
        if arr_string[j] == chr(i):
            print(j, end=" ")
            being = True
            break
    # convey data from inside loop block to outside of it using the variable
    # which was declared before the block
    if being == False: 
        print(-1, end=" ")