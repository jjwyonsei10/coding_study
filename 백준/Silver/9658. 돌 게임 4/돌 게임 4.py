n = int(input())
ans = ["SK", "CY"]
cnt = 0
dp = [0,1,0,1,0,0,0,0]
#0번째는 없고 이제 1부터 7까지의 값을 정함

n %= 7
if n == 0:
    n+=7
print(ans[dp[n]])