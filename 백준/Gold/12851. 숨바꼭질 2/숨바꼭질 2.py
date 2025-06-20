from collections import deque
s,e = map(int, input().split())
arr = [0] * (100001)
visit = [0] * (100001)
def bfs(s,e):
    q = deque()
    q.append(s)
    visit[s] = 1
    while q:
        x = q.popleft()
        if x == e:
            return arr[x]
        for nx in (x-1, x+1, x*2):
            if 0<=nx <= 100000:
                if not arr[nx]:
                    arr[nx] = arr[x] + 1
                    visit[nx] = visit[x]
                    q.append(nx)
                elif arr[nx] == arr[x] + 1:
                    visit[nx] += visit[x]
bfs(s,e)
print(arr[e])
print(visit[e])