t = int(input())

moi = lambda: map(int, input().split())

for _ in range(t):
    n = int(input())
    arr1 = list(moi())
    arr2 = list(moi())

    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = arr1[0]
    dp[0][1] = arr2[0]
    if n == 1:
        print(max(dp[0][0], dp[0][1]))
        continue

    dp[1][0] = dp[0][1] + arr1[1]
    dp[1][1] = dp[0][0] + arr2[1]

    if n == 2:
        print(max(dp[1][0], dp[1][1]))
        continue

    for i in range(2, n):
        dp[i][0] = max(dp[i-1][1], dp[i-2][1])+ arr1[i]
        dp[i][1] = max(dp[i-1][0], dp[i-2][0]) + arr2[i]
    print(max(dp[-1][0], dp[-1][1]))