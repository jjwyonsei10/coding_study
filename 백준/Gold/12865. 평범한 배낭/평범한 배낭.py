moi = lambda: map(int, input().split())
n, m = moi()
w = []
v = []
for _ in range(n):
    a,b = moi()
    w.append(a)
    v.append(b)
dp = [0] * (m+1)
for i in range(n):
    for limit in range(m, 0, -1):
        if limit >= w[i]:
            dp[limit] = max(dp[limit], dp[limit - w[i]] + v[i])
print(dp[-1])
