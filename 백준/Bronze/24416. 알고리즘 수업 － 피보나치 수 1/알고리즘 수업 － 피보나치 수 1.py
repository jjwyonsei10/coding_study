dp = [0] *41
cnt = 0
cnt1 = 0
def fibo(n):
    global cnt
    dp[1]=dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        cnt+=1
    return dp[n]

def fibo1(n):
    global cnt1
    if n == 1 or n == 2: 
        return 1
    else:
        cnt1+=1
        return fibo1(n-1) + fibo1(n-2)

n = int(input())
fibo(n)
fibo1(n)
print(cnt1+1, cnt)
