n = int(input())

if (n % 4)==0:
    repeat = n // 4
else:
    repeat = (n // 4) + 1

for i in range(repeat):
    print("long", end=" ")
print("int")