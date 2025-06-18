n  = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [0] * n
def dfs(x):
    for i in range(n):
        if arr[x][i] and not visit[i]:
            visit[i] = 1
            dfs(i)
for i in range(n):
    dfs(i)
    print(*visit)
    visit = [0] * n