import sys

n = int(input())
hs = list(map(int, input().split()))

best = hs[0]

sum = 1
res = 0
for i in hs[1:]:
    if i <= best:
        sum += 1
    else:
        res += sum * best
        sum = 1
        best = i

if sum != 1:
    if best == hs[n-1]:
        res += best * (sum - 1)
    else:
        hs.reverse()
        sum = 0
        best = hs[n-1]
        for i in enumerate(hs):
            if i <= best:
                sum += 1
            else:
                res += sum * best
                sum = 1
                best = i

print(res)
