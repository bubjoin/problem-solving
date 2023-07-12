numbers = []
for i in range(7):
    numbers.append(int(input()))

odd_numbers = []
for num in numbers:
    if (num % 2) == 1:
         odd_numbers.append(num)

if len(odd_numbers)!=0:
    sum_odd = sum(odd_numbers)
    
    odd_numbers.sort()
    min_odd = odd_numbers[0]

if len(odd_numbers) == 0:
    print(-1)
else:
    print(sum_odd)
    print(min_odd)