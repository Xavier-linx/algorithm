from os import read
import sys

n, m = map(int, input().split())

loc = sorted(list(map(int, input().split())))

i, j = 0, 0
pre = loc[0]
res = 0
ready = False
k = 0
while k < n:
    while loc[k] - pre < m:
        k += 1
        if k >= n:
            res += 1
            break
    if k >= n:
        # res += 1
        break
    pre = loc[k]
    res += 1
    k += 1
    if k >= n:
        # res += 1
        break
    while loc[k] - pre <= m:
        k += 1
        if k >= n:
            res += 1
            break
    if k >= n:
        # res += 1
        break
    pre = loc[k]
# if loc[n-1] - pre > m:
#     res += 1
print(res)


        


