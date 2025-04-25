n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s,e = 1, max(arr)
while s<=e:
    cnt = 0
    mid = (s+e)//2
    for a in arr:
        if a> mid:cnt+= (a-mid)
    if cnt >=m:s = mid+1
    else:e = mid-1
print(e)