"""
input:
5
1 2 3 4 5
output:
10
input:
6
3 1 2 5 4 5
output:
19
"""


# import sys

# n = int(input())
# hs = list(map(int, input().split()))

# best = hs[0]

# sum = 1
# res = 0
# for i in hs[1:]:
#     if i <= best:
#         sum += 1
#     else:
#         res += sum * best
#         sum = 1
#         best = i

# if sum != 1:
#     if best == hs[n-1]:
#         res += best * (sum - 1)
#     else:
#         sum = 0
#         best = hs[n-1]
#         for i in hs[:sum:-1]:
#             if i <= best:
#                 sum += 1
#             else:
#                 res += sum * best
#                 sum = 1
#                 best = i

# print(res)




# n = input()
# dangban = list(map(int,input().split()))
# right = len(dangban)
# left = 0
# max_left = 0
# max_right = 0
# #左数组
# leftsize = []
# rightsize = []
# for left in range(len(dangban)-1):
#     max_left = max(dangban[left],max_left)
#     leftsize.append(max_left)
# for right in range(len(dangban)-1,0,-1):
#     max_right = max(dangban[right],max_right)
#     rightsize.append(max_right)
# sum = 0
# rightsize = rightsize[::-1]
# for i in range(len(dangban)-1):
#     sum = min(leftsize[i],rightsize[i])+sum
 
# print(sum)