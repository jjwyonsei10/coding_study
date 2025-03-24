import sys
sys.setrecursionlimit(10000000)

input = sys.stdin.readline


n  = int(input())

moi = lambda: map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = moi()
    graph[a].append(b)
    graph[b].append(a)

visit = [0] * (n+1)
dp = [[0,1] for _ in range(n+1)]

def dfs(x):
    visit[x] = 1
    for next in graph[x]:
        if visit[next]: continue
        dfs(next)
        dp[x][0]+= dp[next][1]
        dp[x][1]+= min(dp[next])

dfs(1)
print(min(dp[1]))