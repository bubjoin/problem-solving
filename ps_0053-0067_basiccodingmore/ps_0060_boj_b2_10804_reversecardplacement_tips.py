# Card place 1-20 to index 0-19
import sys

cards = [i + 1 for i in range(20)]

for i in range(10):
    begin, end = map(int, sys.stdin.readline().split())
    begin = begin - 1
    end = end - 1
    length = end - begin + 1
    change = length // 2 # remember this pattern, change n times
    # abcde -> e bcd a -> e d c b a, change 2 times
    # abcd -> d bc a -> d c b a, change 2 times
    for i in range(change):
        # cards[begin], cards[end] = cards[end], cards[begin]
        temp = cards[begin]
        cards[begin] = cards[end]
        cards[end] = temp
        
        begin = begin + 1  # should go right
        end = end - 1      # should go left

for i in range(len(cards)):
    print(cards[i], end= " ")