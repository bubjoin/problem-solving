import sys
input = sys.stdin.readline

N, M = map(int, input().split())

ANS = list(map(int, input().split()))

MODELS = []

for i in range(N):
    MODEL = list(map(int, input().split()))
    MODELS.append(MODEL)

# print(MODELS)

# max single model precision
max_smp = 0

for model in MODELS:
    smp = 0
    for m in range(M):
        if model[m]==ANS[m]:
            smp += 1
    if smp > max_smp:
        max_smp = smp



# 
combination = []

