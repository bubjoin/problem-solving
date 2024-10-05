# Trying an idea
# Not implemented properly
# But lead to another idea as right answer

import sys
input = sys.stdin.readline

N = int(input().strip())

# N <= 1_000_000

claps = 0

d1_clap_q = (N // 10) * 3
d1_clap_r = (N % 10) // 3

d10_clap_q = (N // 100) * 30 
d10_clap_r = ((N % 100) >= 90) * (20 + ((N%10)+1)) or \
             ((N % 100) >= 60) * (10 + ((N%10)+1)) or \
             ((N % 100) >= 30) * ( 0 + ((N%10)+1)) or \
             0

d100_clap_q = (N // 1000) * 300
d100_clap_r = ((N % 1000) >= 900) * (200 + ((N%100)+1)) or \
              ((N % 1000) >= 600) * (100 + ((N%100)+1)) or \
              ((N % 1000) >= 300) * ( 0 + ((N%10)+1)) or \
              0

claps = d1_clap_q + d1_clap_r + d10_clap_q + d10_clap_r

print(claps)