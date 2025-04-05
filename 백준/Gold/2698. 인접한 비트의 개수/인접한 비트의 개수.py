t = int(input())

dp  = [[[0,0] for _ in range(101)] for _ in range(101)]
dp[1][0][1] = 1
dp[1][0][0] = 1

for j in range(101):
    for i in range(2, 101):
        if j == 0:
            dp[i][j][1] = dp[i-1][j][0] # j = 0일때, 맨 마지막에 1이 있다는 것은 죄측에 0이라는 뜻
        else:
            dp[i][j][1] = dp[i-1][j-1][1] + dp[i-1][j][0] # j > 0, 맨마지막에 1이 있다는 것 = 그전에 것에서  j-1, 그 후에는 0이 있고 j개 있다는것 
        dp[i][j][0] = dp[i-1][j][1] + dp[i-1][j][0] # 0인 경우, 그전에 j개의 비트가 존재해야 함.

for _ in range(t):
    n,k = map(int, input().split())
    res = dp[n][k][1] + dp[n][k][0]
    print(res)