for m in dir(set()):
    print(m)

sides=frozenset({2,1,3})
triangles=set()
triangles.add(sides)
sides=frozenset({1,2,3})
triangles.add(sides)
print(triangles)

# set in set error(also set as key)
# use frozenset instead
#
# similarly, unhashable type list
# use tuple instead

from math import sqrt

N, M = map(int, input().split())

triangles=set()

for ax in range(N+1):
    for ay in range(M+1):
        for bx in range(N+1):
            for by in range(M+1):
                for cx in range(N+1):
                    for cy in range(M+1):
                        # add condition to exclude diagonal
                        if ((ax, ay)!=(bx, by)) and ((cx, cy)!=(bx, by)) and ((cx, cy)!=(ax, ay)):
                            straight=False
                            try:
                                slope1=(ay-by)/(ax-bx)
                            except:
                                slope1=None
                            try:
                                slope2=(by-cy)/(bx-cx)
                            except:
                                slope2=None
                            if slope1==slope2:
                                straight=True
                            if straight==False:
                                sides=[sqrt((ax-bx)**2+(ay-by)**2), sqrt((cx-bx)**2+(cy-by)**2), sqrt((cx-ax)**2+(cy-ay)**2)]
                                sides.sort()
                                sides=tuple(sides)
                                triangles.add(sides)

# for t in triangles:
#     print(t)
print(len(triangles))
