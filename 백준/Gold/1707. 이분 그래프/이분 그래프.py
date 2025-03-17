import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

t = int(input())
flag = True
def dfs(x):
    global flag
    visit[x] = 1

    for i in graph[x]:
        if not visit[i]:
            visit[i] = 1
            color[i] = color[x] ^ 1
            dfs(i)
        else:
            if color[i] == color[x]:
                flag = False

for _ in range(t):
    flag= True
    n,m = map(int, input().split())

    graph = [[] for _ in range(n+1)]

    for i in range(m):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    
    visit = [0] * (n+1)
    color = [0] * (n+1)

    for i in range(1, n+1):
        if not visit[i]:
            dfs(i)
    
    if flag:
        print("YES")
    else:
        print("NO")