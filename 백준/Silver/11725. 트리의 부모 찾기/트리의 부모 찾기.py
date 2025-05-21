import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())

moi = lambda :map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = moi()
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n+1)

def dfs(node):
    #생각해봐라, parent를 출력해야 한다
    for child in graph[node]:
        if not parent[child]: #부모가 아니다
            parent[child] = node
            dfs(child)

dfs(1)
for i in range(2, n+1):
    print(parent[i])