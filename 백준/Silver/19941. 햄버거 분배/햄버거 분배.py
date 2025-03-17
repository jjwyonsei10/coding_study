n,m = map(int, input().split())

s = input().rstrip()
cnt = 0
dp = [0] * (n)
for i in range(n):
    if s[i] == 'P':
        for j in range(i-m, i+m+1):
            if 0<=j<n and s[j] == 'H' and dp[j] == 0:
                dp[j]=1
                cnt+=1
                break
print(cnt)