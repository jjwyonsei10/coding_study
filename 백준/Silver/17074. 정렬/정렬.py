import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = []
for i in range(1, n):
    if arr[i-1] <= arr[i]:
        dp.append(0)
    else:
        dp.append(1)
res = []
for i in range(len(dp)):
    if dp[i] == 1:
        res.append(i)
cnt = 0
if len(res) == 1:
    id = res.pop()
    for k in range(id, id+2):
        dp = [0] * (n-1)
        tmp = arr[:k] + arr[k+1:]
        check = True
        for i in range(n-2):
            if tmp[i] > tmp[i+1]:
                check= False
        if check:
            cnt+=1
    print(cnt)
elif len(res) > 1:
    print(0)
else:
    print(n)
