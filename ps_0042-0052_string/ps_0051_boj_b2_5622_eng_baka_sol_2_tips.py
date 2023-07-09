# If the intervals between the boundaries are not constant,
# use an index that numbers the boundaries in order

dial = [ord(c) for c in ['a','d','g','j','m','p','t','w','{']]
word = list(input().lower())

total_time = 0
for c in word:
    for i in range(len(dial)):
        if ord(c) < dial[i]:
            total_time += i + 2
            break

print(total_time)