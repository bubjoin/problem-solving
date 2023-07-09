import sys
a, b = map(int, sys.stdin.readline().split())
c = int(input())

h, m = a, b
t = c

fin_time = 60*h + m + t

fin_h = (fin_time // 60) % 24
fin_m = fin_time % 60

print(fin_h, fin_m, sep=" ")