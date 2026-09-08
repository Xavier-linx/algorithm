import sys

T = list(input())
S = list(input())

dp = [[0] *(len(S)+1) for _ in range(len(T)+1)]

for i in range(1, len(T) +1):
    for j in range(1, len(S) +1):
        if T[i-1] == S[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
            print(T[i-1])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

for i in dp:
    print(i)
print(len(T) - dp[len(T)][len(S)])