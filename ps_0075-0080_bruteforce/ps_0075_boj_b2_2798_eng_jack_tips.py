# Sort
# If you find more math
# You can get more speed
import sys
n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

cards.sort()

largest = 0

for i in range(n-2):
    if cards[i] > (m-5):
        break
    for j in range(i+1, n-1):
        if (cards[i] + cards[j]) > (m-3):
            break
        for k in range(n-1, j, -1):
            sum = cards[i] + cards[j] + cards[k]
            if (sum <= m):
                if sum > largest:
                    largest = sum
                break

print(largest)