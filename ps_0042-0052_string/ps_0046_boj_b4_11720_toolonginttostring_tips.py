# How can you deal with a 100-digit number
# if it is not Python?
# Make it string

n = int(input())
numbers_string = input()

# numbers_list = list(map(int, list(numbers_string)))
# the below also works
numbers_list = list(map(int, numbers_string)) # "12345" => [1, 2, 3, 4, 5]

sum = 0
for i in range(n):
    sum += numbers_list[i]
    
print(sum)