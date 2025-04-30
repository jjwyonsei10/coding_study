import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for diag in range(n-1):#대각선을 본다(0~n-1까지)
    for i in range(n-1-diag):
        j = diag + i + 1
        #print(diag,i,j)
        dp[i][j] = 2**31
        for k in range(i,j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + arr[i][0] * arr[k][1] * arr[j][1])
print(dp[0][n-1])