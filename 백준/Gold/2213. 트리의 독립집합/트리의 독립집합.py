import sys
input = sys.stdin.readline

moi = lambda: map(int, input().split())

n = int(input())

arr = [0] + list(moi())

adj = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = moi()
    adj[a].append(b)
    adj[b].append(a)

dp = [[0,0] for _ in range(n+1)]
visit = [0] * (n+1)


def dfs(x):
    if visit[x]:
        return max(dp[x])
    visit[x] = 1
    dp[x][1]= arr[x]
    for child in adj[x]:
        if not visit[child]:
            dfs(child)
            dp[x][0]+= max(dp[child])
            dp[x][1]+= dp[child][0]
            
    return max(dp[x])


res = dfs(1)

trace_res  = []
check = [0] * (n+1)

def traces(cur, pre):
    check[cur] = 1
    if pre == 1:
        for child in adj[cur]:
            if not check[child]:
                traces(child, 0)
    else:
        #포함되는 경우
        if dp[cur][0] < dp[cur][1]:
            trace_res.append(cur)
            for child in adj[cur]:
                if not check[child]:
                    traces(child, 1)
        else:
            #포함 안되는 경우
            for child in adj[cur]:
                if not check[child]:
                    traces(child, 0)

traces(1, 0)
trace_res.sort()
print(res)
print(*trace_res)