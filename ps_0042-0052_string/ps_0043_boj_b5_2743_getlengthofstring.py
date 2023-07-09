# string length without the last '\n'

string = input()
# print(len(string))
# OR

length = 0
string = list(string)

# cf.
# there is a NULL character at the end of a string in C
# to check the end of the string
for character in string:
    length += 1

print(length)