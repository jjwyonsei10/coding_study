le = input().rstrip()
n = len(le)
palin = [[0] * n for  _ in range(n)]
dp = [2500] * (n+1)
dp[-1] = 0

for e in range(n):
    for s in range(e+1):
        if le[e] == le[s] and (e-s < 2 or palin[s+1][e-1]):
            palin[s][e] = 1
            dp[e] = min(dp[e], dp[s-1] + 1)
print(dp[n-1])