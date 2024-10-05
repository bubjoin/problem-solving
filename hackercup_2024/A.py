# Subsonic Subway

input_lines = []
output_lines = []

with open("./hackercup_2024/subsonic_subway_input.txt", "rt") as f:
    for line in f:
        input_lines.append(line)


T = int(input_lines.pop(0))

# caution 2: invert t <-> m to get answer slope

for t in range(T):
    N = int(input_lines.pop(0))
    windows = []
    for n in range(N):
        window = list(map(int, input_lines.pop(0).split()))
        windows.append(window)
    
    slopes = []
    for i in range(len(windows)): # caution 1: index 0 is 1 mile
        slope = [windows[i][0]/(i+1), windows[i][1]/(i+1)]
        slopes.append(slope)
    
    narrow = [0, 1_000_000]
    answer = 0
    for i in range(len(slopes)):
        if (slopes[i][0] > narrow[1]) or (slopes[i][1] < narrow[0]):
            answer = -1
            break
        if (slopes[i][1] <= narrow[1]) and (slopes[i][1] >= narrow[0]):
            if slopes[i][1] <= narrow[1]:
                narrow[1] = slopes[i][1]
        if (slopes[i][0] <= narrow[1]) and (slopes[i][0] >= narrow[0]):
            if slopes[i][0] >= narrow[0]:
                narrow[0] = slopes[i][0]

    if answer == -1:
        output_lines.append(f'Case #{t+1}: -1')
    else:
        the_index = 0
        for i in range(len(slopes)):
            if slopes[i][1]==narrow[1]:
                the_index = i
                break
        answer = (the_index + 1)/windows[the_index][1]
        output_lines.append(f'Case #{t+1}: {answer}')

with open("./hackercup_2024/subsonic_subway_output.txt", "wt") as f:
    for line in output_lines:
        f.write(line + '\n')