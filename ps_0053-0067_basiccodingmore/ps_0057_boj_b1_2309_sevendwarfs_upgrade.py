nine_dwarfs = []
for i in range(9):
    nine_dwarfs.append(int(input()))

sum_nine = sum(nine_dwarfs)

seven_dwarfs_list = [] # to find all possible answer

for i in range(len(nine_dwarfs)):
    for j in range((i + 1), len(nine_dwarfs)):
        check_hundred = sum_nine - nine_dwarfs[i] - nine_dwarfs[j]
        if check_hundred == 100:
            seven_dwarfs = nine_dwarfs.copy()            
            seven_dwarfs[i] = 0
            seven_dwarfs[j] = 0
            seven_dwarfs.sort()
            del seven_dwarfs[:2]
            seven_dwarfs_list.append(seven_dwarfs)
    
# for seven_dwarfs in seven_dwarfs_list:
#     print(seven_dwarf)

for dwarf in seven_dwarfs_list[0]:
    print(dwarf)