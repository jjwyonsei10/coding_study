N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

s,e = 1, max(arr)

while s<=e:
    mid = (s+e)//2
    cnt = 0
    for a in arr:
        cnt+= (a//mid)
    if cnt >= M:
        s = mid+1
    else:
        e = mid-1
print(e)