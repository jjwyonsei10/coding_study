t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if j == i+1: dp[i][j] = arr[i] + arr[j]
    
    for i in range(n-1, 0, -1):
        for j in range(1,n+1):
            if dp[i][j] == 0 and j > i:
                dp[i][j] = min([dp[i][k] + dp[k+1][j] for k in range(i,j)] ) + sum(arr[i:j+1])
    print(dp[1][n])