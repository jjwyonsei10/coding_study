import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)
moi = lambda: map(int, input().split())
n,m = moi()
maps =[list(moi()) for _ in range(n)]
visit = [[-1] * (m) for _ in range(n)] # visit
def dfs(x,y):
    global visit
    if x == n-1 and y == m-1:
        return 1
    if visit[x][y] == -1:
        visit[x][y] = 0
        for nx, ny in ((x-1, y), (x+1, y), (x, y+1), (x, y-1)):
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] < maps[x][y]:
                visit[x][y]+= dfs(nx,ny)
    return visit[x][y]
print(dfs(0,0))