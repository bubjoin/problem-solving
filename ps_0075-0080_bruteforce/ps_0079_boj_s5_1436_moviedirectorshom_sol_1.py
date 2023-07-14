n = int(input())

number = 665
while n > 0:
    number += 1
    number_array = []
    for i in range(len(str(number))):
        number_array.append(str(number)[i])
    
    for i in range(len(number_array)-2):
        if number_array[i] == '6':
            if number_array[i+1] == '6':
                if number_array[i+2] == '6':
                    n = n - 1
                    break
    
print(number)