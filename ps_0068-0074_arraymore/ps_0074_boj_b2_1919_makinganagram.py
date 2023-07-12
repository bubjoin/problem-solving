word_1 = input()
word_2 = input()

alphabet_1 = [0 for i in range(26)]
alphabet_2 = [0 for i in range(26)]

for c in word_1:
    alphabet_1[ord(c) - 97] += 1

for c in word_2:
    alphabet_2[ord(c) - 97] += 1
    
n_del = 0

for i in range(26):
    n_del += max(alphabet_1[i], alphabet_2[i]) \
        - min(alphabet_1[i], alphabet_2[i])

print(n_del)