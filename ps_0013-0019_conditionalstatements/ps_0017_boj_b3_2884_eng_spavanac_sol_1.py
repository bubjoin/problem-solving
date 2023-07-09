import sys
h, m = map(int, sys.stdin.readline().split())

time = h*60 + m
new_time = time - 45

if new_time >= 0:
    new_h = new_time // 60
    new_m = new_time % 60
else:
    new_h = 23
    new_m = 60 + new_time

print(f"{new_h} {new_m}")