t = int(input())

for i in range(t):
    cnt_right_place = 0
    
    place_a, place_b, place_c = list(input())
    
    if place_a == 'a':
        cnt_right_place += 1
    if place_b == 'b':
        cnt_right_place += 1
    if place_c == 'c':
        cnt_right_place += 1
    
    if cnt_right_place >= 1:
        print('YES')
    else:
        print('NO')
