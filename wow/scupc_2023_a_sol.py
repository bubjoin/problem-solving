# b, s, a

# b, s, a
# scu

interest = {'b':0, 's':0, 'a':0}

N = int(input())
string = input().lower()

for c in string:
    if c=='b':
        interest['b'] += 1
    elif c=='s':
        interest['s'] += 1
    else:
        interest['a'] += 1
        

B = interest['b']
S = interest['s']
A = interest['a']
MAX = max(B,S,A)

if (B==S) and (S==A):
    print("SCU")
elif (MAX==B) and (B==S):
    print("BS")
elif (MAX==S) and (S==A):
    print("SA")
elif (MAX==A) and (B==A):
    print("BA")
else:
    if MAX==B:
        print('B')
    elif MAX==S:
        print('S')
    else:
        print('A')
