import sys
input = sys.stdin.readline
train = int(input())
for t in range(train):
    n = int(input())
    arr = list()
    cnt  = n//10 + 1 if n%10 else n//10
    for _ in range(cnt): arr += list(map(int, input().split()))
    dp = [0] * (n)
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = dp[i-1] + arr[i]
    total_sum = dp[-1]

    for ind in dp:
        if total_sum % ind == 0:
            cnt = 0
            for val in dp:
                if val%ind == 0:
                    cnt+=1
            if cnt == total_sum//ind:
                print(ind)
                break