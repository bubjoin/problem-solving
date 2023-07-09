import sys
n = int(input())
scores = list(map(int, sys.stdin.readline().split()))

best_score = max(scores)

for i in range(n):
    scores[i] = scores[i] / best_score * 100

sum = 0
for new_score in scores:
    sum += new_score
    
average = sum / n

print(average)