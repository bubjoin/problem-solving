id = input() # input() does not read the last '\n'
# cf) sys.stdin.readline() includes the '\n'

print("".join([id, "??!"])) # id+"??!", or f"{id}??!"