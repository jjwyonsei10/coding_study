#개인적으로 봤을때, 이 문제는 그냥 구역을 찾는 문제에 가깝다.
import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visit[x][y] = 1
    while q:
        x,y = q.popleft()
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0<=nx<n and 0<=ny< m and arr[nx][ny] and not visit[nx][ny]:
                visit[nx][ny] = 1
                q.append([nx, ny])
for _ in range(t):
    cnt = 0
    m,n,k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    visit = [[0] * m for _ in range(n)]
    for _ in range(k):
        y,x = map(int, input().split())
        arr[x][y] = 1
    for i in range(n):
        for j in range(m):
            if not visit[i][j] and arr[i][j]:
                bfs(i,j)
                cnt+=1
    print(cnt)
