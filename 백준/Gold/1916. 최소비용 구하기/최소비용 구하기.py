import heapq

n = int(input())
t = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(t):
    a,b,c = map(int, input().split())
    arr[a].append((b,c))
s,e = map(int, input().split())
def dijk(s,e):
    visit= [int(1e9)]* (n+1)
    q = []
    visit[s] = 0
    heapq.heappush(q, [0, s])
    while q:
        cost, node = heapq.heappop(q)
        if visit[node] < cost: continue
        for nx, ncost in arr[node]:
            cal = ncost + cost
            if visit[nx] > cal:
                visit[nx] = cal
                heapq.heappush(q, (cal, nx))
    return visit[e]
print(dijk(s,e))