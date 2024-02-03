N = int(input())
logo_song = input().lower()

arr = [0] * 26

for c in logo_song:
    code = ord(c)
    if 97 <= code <= 122:
        arr[code-97] += 1

print(max(arr))
