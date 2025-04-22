n,m,k = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]
sum = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if (i+j) % 2 == 0:
            if board[i-1][j-1] == 'B':
                sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]
            else:
                sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]+1
        else:
            if board[i-1][j-1] == 'W':
                sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]
            else:
                sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]+1
min_ = float('inf')
max_ = -float('inf')

for i in range(k, n+1):
    for j in range(k, m+1):
        max_ = max(sum[i][j] - sum[i-k][j] - sum[i][j-k] + sum[i-k][j-k], max_)
        min_ = min(sum[i][j] - sum[i-k][j] - sum[i][j-k] + sum[i-k][j-k], min_)
print(min(min_, max_, k**2 - min_, k**2 - max_))