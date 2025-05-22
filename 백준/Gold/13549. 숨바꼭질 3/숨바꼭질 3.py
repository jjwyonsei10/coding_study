from collections import deque
s,e = map(int, input().split())
MAX = 10**5
visit = [0] * (MAX+1)
q = deque()
q.append(s)
while q:
    x = q.popleft()
    if x == e:
        break
    for nx in (2*x, x-1, x+1):
        if nx < 0 or nx > MAX or visit[nx]: continue
        if nx == 2*x:visit[nx] = visit[x]
        else:visit[nx] = visit[x] + 1
        q.append(nx)
print(visit[e])