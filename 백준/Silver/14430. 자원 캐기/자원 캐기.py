import sys
input = sys.stdin.readline
moi = lambda: map(int, input().split())
n,m = moi()
arr = [list(moi()) for _ in range(n)]
dp  = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + arr[i-1][j-1]
print(dp[n][m])