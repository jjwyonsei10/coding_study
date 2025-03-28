n,t = map(int, input().split())

dp = [0] * (t+1)
dp[0] = 1
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)
for a in arr:
    for i in range(a, t+1):
        dp[i]+= dp[i-a]
print(dp[t]) 
