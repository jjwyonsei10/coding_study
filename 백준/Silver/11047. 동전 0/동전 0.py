n, m = map(int, input().split())

arr = [int(input()) for _ in range(n)]

cnt = 0
while m:
    for i in range(n-1, -1, -1):
        if arr[i] <= m:
            cnt += m//arr[i]     
            m%= arr[i]
print(cnt)