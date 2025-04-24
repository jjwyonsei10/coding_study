moi = lambda: map(int, input().split())

n,m = moi()

arr = [list(moi()) for _ in range(n)]

def multi(x,y):
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                dp[i][k]+= (x[i][j] * y[j][k] % 1000)
    return dp

def square(x, n):
    if n == 1: return x
    tmp = square(x, n//2)
    if n % 2 == 0: return multi(tmp, tmp)
    else: return multi(multi(tmp, tmp), x)

res = square(arr, m)

for i in range(n):
    for j in range(n):
        res[i][j] %= 1000
for r in res:
    print(*r)
