import sys
sys.setrecursionlimit(10**6) 

input = sys.stdin.readline
moi = lambda: map(int, input().split())
n,r,q = moi()
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = moi()
    graph[a].append(b)
    graph[b].append(a)

dp = [0] * (n+1)

def dfs(x):
    dp[x] = 1
    for i in graph[x]:
        if not dp[i]:
            dfs(i)
            dp[x]+= dp[i]

dfs(r)

for _ in range(q):
    a = int(input())
    print(dp[a])