# Tips
# If a problem has no clue about when it ends,
# think about exception handling
# Study EOF in C++ and Python

import sys

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
    except Exception as e:
        # print(e)
        break
    print(a + b)