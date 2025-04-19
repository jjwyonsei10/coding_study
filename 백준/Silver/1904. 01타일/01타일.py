n = int(input())

def fibo(n):
    dp[1]  = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
    return dp[n]

dp = [0] * (1000001)

fibo(n)

print(dp[n])