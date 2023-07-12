# Imagine a problem
# Observe and find a math

# Must do a test case before submit

nine_dwarfs = []
for i in range(9):
    nine_dwarfs.append(int(input()))

sum_nine = sum(nine_dwarfs)

seven_dwarfs = nine_dwarfs.copy()

escape = False # to escape after escaping nested loop
for i in range(len(nine_dwarfs)):
    for j in range((i + 1), len(nine_dwarfs)): # don't choose same dwarf twice
        check_hundred = sum_nine - nine_dwarfs[i] - nine_dwarfs[j]
        if check_hundred == 100:
            
            # never do this comment block,
            # because index value changes after first pop
            # seven_dwarfs.pop(i)
            # seven_dwarfs.pop(j)
            
            seven_dwarfs[i] = 0
            seven_dwarfs[j] = 0
            escape=True
            break # break escapes one loop block in which it is
    if escape:
        break
    
seven_dwarfs.sort()

# debug
# print(seven_dwarfs)

# seven_dwarfs.pop(0)
# seven_dwarfs.pop(0)
del seven_dwarfs[:2]

for dwarf in seven_dwarfs:
    print(dwarf)