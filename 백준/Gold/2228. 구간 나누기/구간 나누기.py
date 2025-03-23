n,m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))
dp = [[-float('inf')] * (m+1) for _ in range(n)]
dp2 = [[-float('inf')] * (m+1) for _ in range(n)]


dp[0][0] = 0
dp2[0][1] = arr[0]

for i in range(1, n):
    dp[i][0] = 0
    dp2[i][0] = -float('inf')
    for j in range(1, min(m, (i + 2) // 2) + 1):
        dp[i][j] = max(dp[i-1][j], dp2[i-1][j])
        dp2[i][j] = max(dp[i-1][j-1] + arr[i], dp2[i-1][j] + arr[i])

print(max(dp[n-1][m], dp2[n-1][m]))