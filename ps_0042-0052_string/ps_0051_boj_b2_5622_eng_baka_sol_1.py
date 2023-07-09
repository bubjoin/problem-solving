word = input().lower()

word = list(word)

total_time = 0

for c in word:
    if ord('a') <= ord(c) <= ord('c'):
        total_time += 3
    elif ord(c) <= ord('f'):
        total_time += 4
    elif ord(c) <= ord('i'):
        total_time += 5
    elif ord(c) <= ord('l'):
        total_time += 6
    elif ord(c) <= ord('o'):
        total_time += 7
    elif ord(c) <= ord('s'):
        total_time += 8
    elif ord(c) <= ord('v'):
        total_time += 9
    elif ord(c) <= ord('z'):
        total_time += 10
    else:
        pass

print(total_time)