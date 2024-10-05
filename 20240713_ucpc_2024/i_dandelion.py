import sys
input = sys.stdin.readline

N = int(input())
garden = set()
garden.add(0)

for i in range(N):
    
    cmd = input()
    if cmd[0]=='L':
        imsi = garden.copy()
        for point in imsi:
            left = point - 1
            if left in garden:
                continue
            garden.add(left)

    elif cmd[0]=='R':
        imsi = garden.copy()
        for point in imsi:
            right = point + 1
            if right in garden:
                continue
            garden.add(right)

    elif cmd[0]=='C':
        cmds = cmd.split()
        seed = int(cmds[1])
        if seed in garden:
            continue
        garden.add(seed)

    else: # Q
        sys.stdout.write(f"{len(garden)}\n")

