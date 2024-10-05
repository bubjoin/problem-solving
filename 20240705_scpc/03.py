
Answer = 0

d_num = int(input())

network =[]

for i in range(d_num+1):
    link = list(map(int, input().split()))
    link.sort()
    network.append(link)

flat = []
for link in network:
    flat = flat + link

d_link_num_list = [0] * d_num


for d in flat:
    d_link_num_list[d-1] += 1


start_end = []

for i in range(d_num):
    if d_link_num_list[i] == 3:
        start_end.append(i+1)

start_end.sort()

network.pop(network.index(start_end))

start = start_end[0]
end = start_end[1]

cnt_path1 = 0


while start!=end:
    for link in network:
        if start in link:
            if link[0] == start:
                start = link[1]
            else:
                start = link[0]
            network.pop(network.index(link))
            cnt_path1 += 1
            break


cnt_path1 -= 1
cnt_path2 = d_num - 2 - cnt_path1

sum = 0
for i in range(1, cnt_path1+1):
    sum += i

Answer += sum

sum = 0
for i in range(1, cnt_path2+1):
    sum += i
    
Answer += sum

print(Answer)
