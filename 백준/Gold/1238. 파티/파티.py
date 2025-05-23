from collections import deque

moi = lambda: map(int, input().split())
n,m,x = moi()
graph = [[] for _ in range(m+1)]
for _ in range(m):
    u,v,c = moi()
    graph[u].append((v,c))
def bfs(s,e):
    q = deque()
    q.append((s,0))
    visit = [int(1e9)] * (n+1)
    while q:
        node,dist = q.popleft()
        if visit[node] < dist: continue
        for nx, cost in graph[node]:
            if visit[nx] > dist + cost:
                visit[nx] = dist+cost
                q.append((nx, cost + dist))
    return visit[e]
res = 0
for i in range(1, n+1):
    if i == x: continue
    go = bfs(x,i)
    back = bfs(i,x)
    res = max(res, go+back)
print(res)