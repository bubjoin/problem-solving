# Line by line

input_lines = []
output_lines = []

with open("./hackercup_2024/line_by_line_validation_input.txt", "rt") as f:
    for line in f:
        input_lines.append(line)


T = int(input_lines.pop(0))

for t in range(T):
    N, P = map(int, input_lines.pop(0).split())
    # 3 10
    # (0.01)**(1/3) - 0.1
    # 0.11544346900318839
    answer = ((((P/100)**(N-1))**(1/N)) - (P/100)) * 100
    output_lines.append(f'Case #{t+1}: {answer}')

with open("./hackercup_2024/line_by_line_validation_output.txt", "wt") as f:
    for line in output_lines:
        f.write(line + '\n')
