# Reduce duplicate calculations

# Check indentation
# Even if you feel like you have no problem with your logic

n, m = map(int, input().split())
whole_board = [input() for i in range(n)]

# White 0, Black 1
# Pre-calculate all coloring counts
check_board = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if ((i+j)%2):
            check = 'B'
        else:
            check = 'W'
        if whole_board[i][j] != check:
            check_board[i][j] = 1

least_paint_count = 64
for i in range(n-7):
    for j in range(m-7):
        paint_count = sum([sum(check_board[line][j:j+8]) for line in range(i, i+8)])
        # If the calcaulted counts are too big
        # Get smaller counts coloring the opposite color
        if paint_count > 32:
            paint_count = 64 - paint_count
        if paint_count < least_paint_count:
            least_paint_count = paint_count

print(least_paint_count)