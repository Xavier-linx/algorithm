"""
100
10
5
2
5
1 2 5 3 4
--
11
--
50
10
10
1
10
1 2 5 3 4 5 4 1 1 1
--
4
--
"""

import math
import bisect
import sys


B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
F = int(sys.stdin.readline())
U = int(sys.stdin.readline())
N = int(sys.stdin.readline())

n = sys.stdin.readline().split()
n = sorted(list(map(int, n)))

left = n[0]
right = n[0] + B

while left <= right:
    mid = (left + right) // 2

    i = bisect.bisect_left(n, mid)
    add = mid * i - sum(n[:i])

    money = add * U + F * math.ceil(float(add) / float(C))

    if money > B:
        right = mid - 1
    elif money < B:
        left  = mid + 1
    else:
        right = mid
        break
    # print(left, right, )

print(right)
# print(money)



