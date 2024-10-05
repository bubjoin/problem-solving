# Line of Delivery

input_lines = []
output_lines = []

with open("./hackercup_2024/line_of_delivery_part_1_input.txt", "rt") as f:
    for line in f:
        input_lines.append(line)


T = int(input_lines.pop(0))

for t in range(T):
    N, G = map(int, input_lines.pop(0).split())
    stones = []
    for n in range(N):
        stones.append(int(input_lines.pop(0)))
    stones.sort(reverse=True)
    dists = []
    for n in range(N):
        dists.append(abs(stones[n]-G))
    idx = dists.index(min(dists))
    output_lines.append(f'Case #{t+1}: {idx+1} {dists[idx]}')


with open("./hackercup_2024/line_of_delivery_part_1_output.txt", "wt") as f:
    for line in output_lines:
        f.write(line + '\n')
