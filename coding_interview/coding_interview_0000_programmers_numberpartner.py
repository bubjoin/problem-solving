def solution(X, Y):
    answer = ''
    
    digits_x = [0 for i in range(10)]
    digits_y = [0 for i in range(10)]
    digits_partner = [0 for i in range(10)]
    
    x = list(map(int, list(str(X))))
    y = list(map(int, list(str(Y))))
    
    # print(x)
    # print(y)
    
    for d in x:
        digits_x[d] += 1
    
    for d in y:
        digits_y[d] += 1
    
    # print(digits_x)
    # print(digits_y)
    
    for i in range(10):
        digits_partner[i] = min(digits_x[i], digits_y[i])
    
    # print(digits_partner)
    
    if sum(digits_partner) == 0:
        answer = '-1'
    elif (sum(digits_partner[1:])==0):
        answer = '0'
    else:
        # print('business logic')
        for i in range(9, -1, -1): # backstep -1
            if digits_partner[i]!=0:
                # print(i)
                part = f"{i}" * digits_partner[i]
                answer += part
    
    return answer


print(solution("100", "123450"))