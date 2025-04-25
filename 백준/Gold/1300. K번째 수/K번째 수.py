n = int(input())
k = int(input())
s,e = 0, k
ans = 0
while s<=e:
    mid = (s+e)//2
    cnt = 0
    for i in range(1, n+1):cnt+= min(n, mid//i)
    if cnt >= k:
        e = mid-1
        ans = mid
    else:
        s = mid+1
print(s)

