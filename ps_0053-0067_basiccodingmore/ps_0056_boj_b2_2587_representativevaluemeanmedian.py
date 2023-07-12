numbers = []
for i in range(5):
    numbers.append(int(input()))

mean = sum(numbers) / len(numbers)
mean = int(mean)

numbers.sort()
median = numbers[int(len(numbers)/2)]

print(mean)
print(median)