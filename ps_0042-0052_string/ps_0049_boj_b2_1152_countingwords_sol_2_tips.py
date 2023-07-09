sentence_to_arr = list(input())

words_list = []
word = []

for i in range(len(sentence_to_arr)):
    if sentence_to_arr[i] != " ": # not a space
        word.append(sentence_to_arr[i])
    else:
        if len(word) > 0:
            words_list.append(word)
        word = []

# imagine the conditions when it ends
# case 1: ends with " "(a space)
# case 2: ends with a character
# for the case 2, the next two lines are needed
if len(word) > 0:
    words_list.append(word)

print(len(words_list))