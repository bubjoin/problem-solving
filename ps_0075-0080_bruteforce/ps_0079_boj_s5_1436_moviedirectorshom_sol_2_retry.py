n = int(input())

number = 665
while n > 0:
    number += 1
    number = str(number)
    if '666' in number:
        n = n -1
    number = int(number)
    
print(number)