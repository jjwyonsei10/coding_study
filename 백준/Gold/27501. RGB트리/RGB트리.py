import sys
input=  sys.stdin.readline

n = int(input())
moi = lambda: map(int, input().split())

graph=  [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = moi()
    graph[a].append(b)
    graph[b].append(a)

dp = [[0,0,0]]

for i in range(n):
    dp.append(list(moi()))

colors = [-1] * (n+1)
visit = [0] * (n+1)
def dfs(x):
    visit[x] = 1
    for i in graph[x]:
        if not visit[i]:
            dfs(i)
            for k in range(3):   
                dp[x][k]+=max(dp[i][k-1], dp[i][k-2])

def path_find(root, color):
    colors[root] = color
    visit[root] = 1
    for i in graph[root]:
        if not visit[i]:
            next_color = (color+1) % 3 if dp[i][(color+1) % 3] > dp[i][(color+2) % 3] else (color+2) % 3
            path_find(i, next_color)
dfs(1)
visit = [0] * (n+1)

root_color = dp[1].index(max(dp[1]))
print(max(dp[1]))
path_find(1, root_color)

for i in range(1, n+1):
    if colors[i] == 0:
        print('R', end = "") 
    elif colors[i] == 1:
        print('G', end = "")
    else:
        print('B', end = "")