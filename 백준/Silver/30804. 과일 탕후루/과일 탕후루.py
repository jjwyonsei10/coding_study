n = int(input())

arr = list(map(int, input().split()))
l = 0
res = {}
ans = 0
for r in range(n):
    if arr[r] in res:
        res[arr[r]]+=1
    else:
        res[arr[r]] = 1

    while len(tuple(res)) > 2:
        res[arr[l]]-=1
        if res[arr[l]] == 0:
            del res[arr[l]]
        l+=1
    ans = max(ans, r-l + 1)
print(ans)