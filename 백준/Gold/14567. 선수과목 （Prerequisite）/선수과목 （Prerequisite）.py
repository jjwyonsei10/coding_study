import sys
from collections import deque
input = sys.stdin.readline

moi = lambda: map(int, input().split())

n,m = moi()
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
parent = [-1] * (n+1)
for _ in range(m):
    a,b = moi()
    indegree[b]+=1
    graph[a].append(b)

dp = [0] * (n+1)

def bfs():
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i]=1
    while q:
        x = q.popleft()
        for nx in graph[x]:
            indegree[nx]-=1
            dp[nx] = max(dp[nx], dp[x] + 1)
            if not indegree[nx]:
                q.append(nx)
bfs()
print(*dp[1:])