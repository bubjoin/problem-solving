
Answer=''
s_num = int(input())
s = list(map(int, input().split()))
s = [0] + s
q_num = int(input())
for i in range(q_num):
    l, r = map(int, input().split())
    s_dict = {}
    q_ans = 0
    
    for j in range(l, r+1):
        if s[j] in s_dict:
            s_dict[s[j]] += 1
        else:
            s_dict[s[j]] = 1

    k_list = list(map(int, s_dict.keys()))
    k_list.sort()

    for k in k_list:
        if k==1:
            continue
        gesu = s_dict[k] // k
        q_ans += gesu

        double_k = k**2
        
        if double_k in k_list:
            s_dict[double_k] += gesu
        
    
    Answer += f'{q_ans}\n'
# print(Answer)

