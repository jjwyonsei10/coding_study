n = int(input())
arr = [0] * n
cnt = 0

def check(x):
    for i in range(x):
        if abs(i - x) == abs(arr[x] - arr[i]) or arr[i] == arr[x]:
            return False
    return True 

def dfs(x):
    global cnt
    if x == n:
        cnt+=1
        return
    for i in range(n):
        arr[x] = i
        if check(x):
            dfs(x+1)
dfs(0)
print(cnt)