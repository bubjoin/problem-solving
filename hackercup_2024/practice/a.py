# Walk the line

input_lines = []
output_lines = []

with open("./hackercup_2024/walk_the_line_input.txt", "rt") as f:
    for line in f:
        input_lines.append(line)

# print(input_lines)

T = int(input_lines.pop(0))

for t in range(T):
    N, K = map(int, input_lines.pop(0).split())
    si = []
    for i in range(N):
        si.append(int(input_lines.pop(0)))
    if N > 2:
        total = (min(si) * (N-2) * 2) + min(si)
    else:
        total = min(si)
    if total <= K:
        output_lines.append(f'Case #{t+1}: YES')
    else:
        output_lines.append(f'Case #{t+1}: NO')
       

# output_lines.append('test')
# output_lines.append('test2')
# output_lines.append('test3')

with open("./hackercup_2024/walk_the_line_output.txt", "wt") as f:
    for line in output_lines:
        f.write(line + '\n')
