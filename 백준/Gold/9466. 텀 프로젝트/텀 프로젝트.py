import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
t = int(input())
cnt = 0

def dfs(x):
    global cnt
    visit[x] = 1
    cycle.append(x)
    if visit[arr[x]]:
        if arr[x] in cycle:
            cnt += len(cycle[cycle.index(arr[x]):])
        return 
    else:
        dfs(arr[x])

for _ in range(t):
    n = int(input())
    cnt = 0
    arr = [0] + list(map(int, input().split()))
    visit = [0]*(n+1)
    for i in range(1, n+1):
        if not visit[i]:
            cycle = []
            dfs(i)
    print(n- cnt)