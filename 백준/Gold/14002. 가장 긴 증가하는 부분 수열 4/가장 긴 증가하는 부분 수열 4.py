import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * (n+1)
parent = [-1] * (n+1)

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            parent[i] = j
            dp[i] = dp[j]+1

ind = dp.index(max(dp))
print(max(dp))
res = [arr[ind]]
cur = parent[ind]
while cur!= -1:
    res.append(arr[cur])
    cur = parent[cur]

print(*res[::-1])