# x != 0
# y != 0

x = int(input())
y = int(input())

if (x > 0) and (y > 0):
    print(1)
elif (x < 0) and (y > 0):
    print(2)
elif (x < 0) and (y < 0):
    print(3)
else: # (x > 0) and (y < 0)
    print(4)