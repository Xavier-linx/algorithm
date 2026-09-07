
"""
input:
6 2
100 200 150 300 250 180
n78 n41 n78 n28 n41 n28
1
n28 n41
output:
450
2 3
input:
3 2
10 10 10
n1 n2 n3
0
output:
20
0 1
"""
import sys
from collections import defaultdict


n, k = map(int, input().split())
rate = list(map(int, input().split()))
names = list(input().split())
conflict = int(input())
conls = []
for _ in range(conflict):
    a, b = input().split()
    conls.append((a, b))


result = 0
resstep = []

def dfs(idx, selected, conf_set, total):
    global result, resstep
    if total > result:
        result = total
        resstep = selected.copy()

    if idx >= n or len(selected) >= k:
        return
    

    name = names[idx]
    if name not in conf_set:
        stop = False
        for conf in conf_set:
            if (name, conf) in conls or (conf, name) in conls:
                stop = True
                break
            
        if not stop:
            selected.append(idx)
            conf_set.add(name)
            dfs(idx+1, selected, conf_set, total+rate[idx])
            selected.pop()
            conf_set.remove(name)
    
    dfs(idx+1, selected, conf_set, total)


dfs(0, [], set(), 0)
print(result)
print(' '.join(map(str, resstep)))

