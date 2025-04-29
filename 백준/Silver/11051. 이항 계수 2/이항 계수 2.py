import sys
input = sys.stdin.readline

n,m = map(int, input().split())
dp = [[0] * (1000+1) for i in range(1000+1)]
dp[0][0] = 1
for i in range(1, n+1):
    dp[i][1] = i  % 10007
    dp[i][i] = dp[i][0] = 1

for i in range(2, n+1):
    for j in range(2, i+1):
        dp[i][j] = (dp[i-1][j-1] % 10007 + dp[i-1][j] % 10007) % 10007
print(dp[n][m])