n = 2
results = []


def generate(open_cnt, close_cnt, seq, results):
    if open_cnt == n and close_cnt == n:
        results.append(seq)
        return
    
    if open_cnt < n :
        generate(open_cnt + 1, close_cnt, seq + '(', results)
    if close_cnt < open_cnt :
        generate(open_cnt, close_cnt + 1, seq + ')', results)

generate(0, 0, '', results)
print(results)


# # test : function flow without explicit return

# test_cnt = 0
# def test():
#     global test_cnt
#     if test_cnt == 2:
#         return
#     print('end')
#     test_cnt += 1
#     test()
#     print("what")

# test()
