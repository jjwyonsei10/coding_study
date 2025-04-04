import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
s,e = map(int, input().split())

dist = [float('inf')] * (n+1)
path = [0] * (n+1)

def dfs(x):
    h = []
    dist[x] = 0
    heapq.heappush(h, (0, x))

    while h:
        cost, node = heapq.heappop(h)
        if cost > dist[node]:
            continue
        for next_node, distance in graph[node]:
            next_cost = cost + distance
            if next_cost < dist[next_node]:
                path[next_node] = node #노드로 하면 그 전에 경로가 사라지고 남지 않는다. 최소인 
                                        #next_node로 잡고 하면 최소인 경우에는 갱신이 되고 아닌 경우에는 기록이 남는다.
                dist[next_node]  = next_cost
                heapq.heappush(h, (next_cost, next_node))
dfs(s)
print(dist[e])
ans = []
cur = e
while cur:
    ans.append(cur)
    cur = path[cur]

print(len(ans))
print(*reversed(ans))