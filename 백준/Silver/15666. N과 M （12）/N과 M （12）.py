n,m = map(int, input().split())

#n,m = 4,2

arr = sorted(list(set(map(int, input().split()))))
#arr = [9,7,9,1]
#arr.sort()
res = []
def dfs(cnt):
    if cnt == m:
        print(*res)
        return
    for i in range(len(arr)):
        if len(res) == 0 or (len(res) and res[-1] <= arr[i]):
            res.append(arr[i])
            dfs(cnt+1)
            res.pop()
dfs(0)
    
