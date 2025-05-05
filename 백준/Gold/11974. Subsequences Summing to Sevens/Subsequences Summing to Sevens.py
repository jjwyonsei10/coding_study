n = int(input())
res = 0
seq = list(int(input()) for _ in range(n))
dp = [0] * (n)
dp[0] = seq[0] % 7
for i in range(1, n):
    dp[i] = (dp[i-1] + seq[i]) % 7
dic = [[] for _ in range(7)]
dic[0].append(-1)
for i in range(n):
    dic[dp[i]].append(i)
res = 0
for i in range(7):
    if dic[i]:
        res = max(res, dic[i][-1] - dic[i][0])
print(res)