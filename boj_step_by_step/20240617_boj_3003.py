chess = list(map(int, input().split()))

# print(chess)

piece = [1, 1, 2, 2, 2, 8]
result = list()

for i in range(6):
    result.append(piece[i] - chess[i])

for n in result:
    print(n, end=' ')