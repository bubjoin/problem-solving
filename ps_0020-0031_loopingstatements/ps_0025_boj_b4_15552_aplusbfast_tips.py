# Tips by jh05013 From BOJ
# Translation and Summary

# The way of doing input/output does matter for timeout

# C++ 
# cin/cout
# both cin.tie(NULL) and sync_with_stdio(false) applied
# and use '\n' instead of endl
# then no more scanf, printf, puts, getchar, putchar, etc. of C input/output

# JAVA
# BufferedReader and BufferedWrite
# instead of Scanner and System.out.println
# use BufferedWriter.flush only one time at the last

# Python
# import sys
# sys.stdin.readline() instead of input()
# sys.stdin.readline() includes the last input character '\n'
# use rstrip() to delete the last '\n' from the string

# For most online judge, input stream != output stream
# You don't have to save all the test case given
# It's O.K that one test case is input and one result is printed

import sys

t = int(input())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)