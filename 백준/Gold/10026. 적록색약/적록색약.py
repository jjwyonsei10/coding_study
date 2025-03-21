from collections import deque
n = int(input())
arr =  [list(input().rstrip()) for _ in range(n)]
visit = [[0]* n for _ in range(n)]

def red_bfs(x,y, color):
    q = deque()
    q.append([x, y])
    visit[x][y] = 1
    while q:
        x,y = q.popleft()
        for nx,ny in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
            if 0<=nx < n and 0<= ny < n and not visit[nx][ny]:
                if (color != 'B' and arr[nx][ny] != 'B') or (color == 'B' and arr[nx][ny] == 'B'):
                    q.append([nx, ny])
                    visit[nx][ny] = 1
    
def bfs(x, y, color):
    q = deque()
    q.append([x, y])
    visit[x][y] = 1
    while q:
        x,y = q.popleft()
        for nx,ny in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
            if 0<=nx < n and 0<= ny < n and color == arr[nx][ny] and not visit[nx][ny]: 
                q.append([nx, ny])
                visit[nx][ny] = 1

cnt = 0
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            bfs(i,j, arr[i][j])
            cnt+=1
visit = [[0]* n for _ in range(n)]
rcnt = 0
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            red_bfs(i,j, arr[i][j])
            rcnt+=1

print(cnt, rcnt)