N,H,K = map(int, input().split())

A = list(map(int, input().split()))


dp = [[0] * N for _ in range(H+1)]

for i in range(N):
    dp[0][i] = 0 if i in A else 1

for h in range(1, H+1):
    for x in range(N):
        dp[h][x] = min(dp[h-1][(x-y) % N] + dp[h-1][y] for y in range(N))

        if x not in A:
            dp[h][x]+= 1
print(min(dp[H]))