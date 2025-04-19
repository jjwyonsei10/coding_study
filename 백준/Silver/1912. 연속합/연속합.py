n = int(input())

dp = [0] * (n+1)

arr = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    dp[i] = max(arr[i], dp[i-1] + arr[i])
print(max(dp[1:]))