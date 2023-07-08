# Long Multiplication
a = int(input())
b = int(input())

d1 = b % 10
d2 = (b // 10) % 10
d3 = b // 100
result = (a * d3) * 100 + (a * d2) * 10 + (a * d1)

print(a * d1)
print(a * d2)
print(a * d3)
print(result)