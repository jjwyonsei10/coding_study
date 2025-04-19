def padoban(n):
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4, n+1):
        dp[i] = dp[i-2] + dp[i-3]

t = int(input())
dp = [0] * (101)
padoban(100)
for _ in range(t):
    n = int(input())
    print(dp[n])