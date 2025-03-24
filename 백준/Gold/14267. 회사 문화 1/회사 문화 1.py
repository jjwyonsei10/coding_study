import sys
sys.setrecursionlimit(1000000)

moi = lambda: map(int, input().split())

n,m = moi()
arr = list(moi())
dp = [0] * (n+1)

graph = [[] for _ in range(n+1)]

for i in range(1, n):
    graph[arr[i]].append(i+1)

for _ in range(m):
    a,b = moi()
    dp[a]+= b
def dfs(x):
    for i in graph[x]:
        dp[i]+= dp[x]
        dfs(i)
dfs(1)
print(*dp[1:])