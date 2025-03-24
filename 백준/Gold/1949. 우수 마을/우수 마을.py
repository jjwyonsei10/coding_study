import sys
input = sys.stdin.readline
n = int(input())
moi = lambda: map(int, input().split())
arr = [0] + list(moi())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = moi()
    graph[a].append(b)
    graph[b].append(a)

parent = [-1] * (n+1)
stack = []

dp = [[0,0] for _ in range(n+1)] 
def dfs(x):
    order = []
    stack.append(x)
    while stack:
        node = stack.pop()
        order.append(node)
        dp[node][1] = arr[node]
        for next in graph[node]:
            if next != parent[node]:
                parent[next]  = node
                stack.append(next)

    for node in reversed(order):
        for next in graph[node]:
            if next!= parent[node]:
                dp[node][0] +=  max(dp[next])
                dp[node][1] +=  dp[next][0]

dfs(1)
print(max(dp[1]))