moi = lambda: map(int, input().split())
n,m = moi()
arr = [int(input()) for _ in range(n)]
arr.sort()
s, e  = 0, arr[-1] - arr[0]
res = 0
while s<= e:
    mid = (s+e)//2
    cnt = 1
    cur = arr[0]
    for i in range(1, n):
        if arr[i] - cur >= mid:
            cnt+=1
            cur = arr[i]
    if cnt >= m:
        s = mid+1
    else:
        e= mid-1
print(e)
