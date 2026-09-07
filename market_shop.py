"""
100
3
10001 1 100 90
10002 2 100 100
10003 3 100 110
---
110
---
200
4
10001 1 200 200
10002 2 10 10
10003 3 10 10
10004 3 10 10
---
230
---
"""


import sys


# B = int(input())
# n = int(input())
# goods = []
# for i in range(n):
#     goods.append(list(map(int, input().split())))
# # id = goods[0]
# cat = [i[1] for i in goods]
# price = [i[2] for i in goods]
# score = [i[3] for i in goods]

lines=sys.stdin.read().strip().splitlines()
b=int(lines[0])
n=int(lines[1])
goods=[]
for line in lines[2:2+n]:
    goods.append(list(map(int,line.split())))
prices=[good[2] for good in goods]
scores=[good[3] for good in goods]
cate=[good[1] for good in goods]

# cat.insert(0, 0)
# price.insert(0, 0)
# score.insert(0, 0)


res = 0
x = 1 << n
for i in range(x):
    top = 0
    tos = 0
    toc = set()
    for j in range(n):
        if (i & (1<<j)):
            toc.add(cate[j])
            top += prices[j]
            tos += scores[j]
    if len(toc) >= 3:
        dis = 30
    else:
        dis = 20

    to_dis = (top//200)*dis
    top -= to_dis
    # print(top)
    if top <= b and res < tos:
        res = tos
            
print(res)


