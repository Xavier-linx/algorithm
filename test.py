import sys

n, m = map(int, input().split())
# values = list(map(int, input().split()))
values = []
while len(values) < n:
    values.extend(map(int, sys.stdin.readline().split()))
values = [0] + values[:n]
if m > n:
    m = n
INF = -10**9
dp = [[INF] * (n+1) for _ in range(m+1)]
dp[0][0] = 0

for i in range(1, m + 1):
    for j in range(i, min(3 * i, n) + 1):
        best = INF
        best = max(dp[i-1][j-1], dp[i-1][j-2], dp[i-1][j-3])
        if best != INF:
            dp[i][j] = best + values[j]

res = dp[m][n]
print(res if res != INF else -1)
