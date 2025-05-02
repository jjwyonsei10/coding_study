import sys
input = sys.stdin.readline
moi = lambda: map(int, input().split())
n,m = moi()
act = [0] + list(moi())
inact = [0] + list(moi())

dp = [[0] * (sum(inact) + 1) for _ in range(n+1)]

res = float('inf')
for i in range(1, n+1):
    now = act[i]
    cost = inact[i]
    for j in range(sum(inact) + 1):    
        if j< cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-cost] + now, dp[i-1][j])

        if dp[i][j] >= m:
            res = min(res, j)
if res == float('inf'):
    print(0) 
else:
    print(res)