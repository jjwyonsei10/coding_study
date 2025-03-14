n,m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
maxvalue = 0
def tetro(x,y, res, cnt):
    global maxvalue
    if cnt == 4:
        maxvalue = max(res, maxvalue)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx< n and 0<=ny < m and not visit[nx][ny]:
            visit[nx][ny] = 1
            tetro(nx, ny, res + arr[nx][ny], cnt+1)
            visit[nx][ny] = 0

def arrow(x,y):
    global maxvalue
    for i in range(4):
        tmp = arr[x][y]
        for j in range(3):
            t = (i+j)%4
            nx = x + dx[t]
            ny = y + dy[t]
            if 0<=nx< n and 0<=ny < m:
                tmp+=arr[nx][ny]
            else:
                tmp = 0
                break
        maxvalue = max(maxvalue, tmp)


for i in range(n):
    for j in range(m):
        if not visit[i][j]:
            visit[i][j] = 1
            tetro(i,j,arr[i][j], 1)
            visit[i][j] = 0

            arrow(i,j)
print(maxvalue)