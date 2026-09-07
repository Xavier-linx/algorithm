import sys


lines=sys.stdin.read().strip().splitlines()
b=int(lines[0])
n=int(lines[1])
goods=[]
for line in lines[2:2+n]:
    goods.append(list(map(int,line.split())))
prices=[good[2] for good in goods]
scores=[good[3] for good in goods]
cate=[good[1] for good in goods]


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

    top = top - (top//200)*dis
    if top <= b and res < tos:
        res = tos
            
print(res)


