a = int(input())
b = int(input())
c = int(input())

mul_abc = a * b * c

# a number -> a string -> mapping int() for each letter -> list
#      123 ->   "123"  -> '1' to 1, '2' to 2, '3' to 3  -> [1, 2, 3]
# map() takes a iterable object like string as second parameter
mul_abc_array = list(map(int, str(mul_abc)))

numbers = [0 for i in range(10)]

for i in range(len(mul_abc_array)):
    for j in range(10):
        if mul_abc_array[i] == j:
            numbers[j] += 1

for i in range(10):
    print(numbers[i])