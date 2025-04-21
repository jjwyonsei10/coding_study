n = int(input())
arr = list(map(int, input().split()))
arr2 = arr[::-1]
dp1 = [1] * (n)
dp2 = [1] * (n)
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:dp1[i] = max(dp1[i], dp1[j]+1)
        if arr2[i] > arr2[j]:dp2[i] = max(dp2[i], dp2[j]+1)
dp2 = dp2[::-1]
res = []
for i in range(n):res.append(dp1[i] + dp2[i]-1)
print(max(res))