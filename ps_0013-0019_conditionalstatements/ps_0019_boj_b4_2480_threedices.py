import sys

d1, d2, d3 = map(int, sys.stdin.readline().split())

if (d1==d2) and (d2==d3):
    prize = 10000 + d1*1000
elif (d1==d2) or (d2==d3) or (d3==d1):
    if (d1==d2) or (d2==d3):
        prize = 1000 + d2*100
    else: # d3==d1
        prize = 1000 + d3*100
else:
    prize = max(d1, d2, d3) * 100
    
print(prize)