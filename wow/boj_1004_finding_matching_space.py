# 20231127
# get each list of planets which start or end point is in
# sort each list along with the radius(short to long)
# get each numbers of circles which a point go through
# to meet the other
# 
# case 1 they have a same circle in common
# get the smallest circle in common 
# and get the sum of the numbers of circles
# each one has to go through
# case 2 they meet out of all the circles in the plane
# get the sum of the numbers of circles each one go through
# to get to the out of all the circles in the plane 
#
# debug twice

import sys

t = int(input())

for test_case in range(t):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(input())
    planets = []
    for i in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split())
        planets.append((cx,cy,r))
    
    start_in = []
    end_in = []
    
    for circle in planets:
        cx, cy, r = circle

        # debug: errata in inequations
        if ((x1-cx)**2 + (y1-cy)**2) < r**2:  
            start_in.append(circle)

        if ((x2-cx)**2 + (y2-cy)**2) < r**2:
            end_in.append(circle)
        
    start_in.sort(key=lambda x:x[2])
    end_in.sort(key=lambda x:x[2])

    # print(start_in)
    # print(end_in)
    
    answer = None
    for s_idx in range(len(start_in)):
        for e_idx in range(len(end_in)):
            if start_in[s_idx] == end_in[e_idx]:
                answer = s_idx + e_idx
                break  # debug: think break condition
        if answer is not None:
            break
    
    if answer is None:
        answer = len(start_in) + len(end_in)
    
    print(answer)
