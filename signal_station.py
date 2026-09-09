from os import read
import sys
import math

n, m = map(int, input().split())

loc = sorted(list(map(int, input().split())))
loc.append(math.inf)

pre = loc[0]
res = 0

k = 1
while k < n:
    while loc[k] - pre <= m:
        k += 1

    pre = loc[k-1]
    res += 1
    # k += 1r
    if k >= n:
        break

    while loc[k] - pre <= m:
        k += 1

    pre = loc[k]
# if loc[n-1] - pre > m:
#     res += 1
if n == 1:
    res = 1
print(res)


        


