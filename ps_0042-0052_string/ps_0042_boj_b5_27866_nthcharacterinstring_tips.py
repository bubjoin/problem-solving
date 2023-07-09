# input() does not takes the last '\n', unlike sys.stdin.readline()
string = input()
nth = int(input())

arr = list(string)

idx = nth - 1 # always keep it in mind

print(arr[idx])