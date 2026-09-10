"""
20
675 889
634 1354
966 1037
529 803
651 675
271 878
1022 1188
703 1408
493 1074
1204 1277
1233 1284
901 904
875 1036
125 443
1277 1301
980 1392
1379 1422
1332 1340
328 641
743 985
--
9
"""

# import sys
# import heapq

# heap = []
# n = int(input())
# for i in range(n):
#     heapq.heappush(heap, tuple(map(int, input().split())))

# # print(heap)
# # print("="*20)
# res = 0
# v1, v2 = 0, 0
# for i in range(n):
#     v1_cur, v2_cur = heapq.heappop(heap)
#     print(v1_cur, v2_cur)
#     if v1_cur - v2 >= 0:
#         res += 1
#         v1 = v1_cur
#         v2 = v2_cur

# print(res)


import sys
import heapq

ls = []
n = int(input())
for i in range(n):
    ls.append(list(map(int, input().split())))

ls.sort(key = lambda x: x[0])

total = 0
def dfs(idx :int, passed: int, last: int):
    global total
    for i in range(idx, n):
        # if i >= n:
        #     return
        dur = ls[i]
        if dur[0] - last >= 0:
            passed += 1
            total = max(passed, total)
            dfs(i+1, passed, dur[1])
            passed -= 1
        # else:
        #     return
        # dfs(passed, last)

# for i in range(n):
#     v = ls[i][1]
dfs(0, 0, 0)
print(total)
