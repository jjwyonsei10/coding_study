moi = lambda: map(int, input().split())
n,m = moi()
arr1 = [list(moi()) for _ in range(n)]
m,r = moi()
arr2 = [list(moi()) for _ in range(m)]
dp = [[0] * r for _ in range(n)]

for i in range(n):
    for j in range(m):
        for k in range(r):
            dp[i][k]+= arr1[i][j] * arr2[j][k]
for d in dp:
    print(*d)