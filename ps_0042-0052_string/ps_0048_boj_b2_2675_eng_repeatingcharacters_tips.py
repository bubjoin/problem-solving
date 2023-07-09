# Alphanumeric(or alphameric) is a character of letter or numeral
# For programming, the alphanumerics are both upper- and lower-case letters,
# 10 numerals, punctuation marks and symbols

import sys

t = int(input())

for i in range(t):
    r, s = sys.stdin.readline().split()
    r = int(r)
    string = str(s).rstrip()
    string_arr = list(string)
    for c in string_arr:
        print(c * r, end="")
    print()