N = int(input())

min_packs = 0

packs = N
pack_5 = 0
pack_3 = 0

for i in range((N//5)+1):
    pack_5 = i
    packs = packs - (5 * i)
    if (packs % 3)==0:
        pack_3 = packs // 3
        min_packs = pack_5 + pack_3
    packs = N

if min_packs==0:
    print(-1)
else:
    print(min_packs)
    
# Retry, think calculation order and end condition to make it faster