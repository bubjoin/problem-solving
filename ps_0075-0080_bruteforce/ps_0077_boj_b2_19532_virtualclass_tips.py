# ax + by = c
# dx + ey = f
#
# x = (c-by)/a
# d(c-by)/a + ey = f
# but, a can be 0

import sys
a, b, c, d, e, f = map(int, sys.stdin.readline().split())

if a == 0: # a can be 0
    y = int(c/b)
    x = int((f-e*c/b)/d)
    print(x, y)
else: 
    # runtime error if a == 0 (zero division)
    for y in range(-999, 1000):
        if (d * (c - b * y) / a + e * y - f) == 0:
            print(int((c-b*y)/a), y)
            break