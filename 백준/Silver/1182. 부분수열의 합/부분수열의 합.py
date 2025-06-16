import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
res = []
cnt = 0
def dfs(x):
    global cnt 
    if sum(res) == m and len(res):
        cnt+=1
    for i in range(x, n):
        res.append(arr[i])
        dfs(i+1)
        res.pop()
dfs(0)
print(cnt)