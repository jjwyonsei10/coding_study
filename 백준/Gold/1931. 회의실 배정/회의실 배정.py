n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key= lambda x: (x[1], x[0]))
res = [[arr[0][0], arr[0][1]]]
for i in range(1, n):
    s,e = arr[i]
    if res[-1][1] <=s:res.append(arr[i])
print(len(res))