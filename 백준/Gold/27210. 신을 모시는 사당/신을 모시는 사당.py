import sys
input = sys.stdin.readline
n = int(input())

arr = list(map(int, input().split()))
cnt = 0
res = 0
min_sum = 0
max_sum = 0
for i in range(n):
    if arr[i] == 1:
        cnt+=1
    else:
        cnt-=1
    
    res = max(res, abs(cnt - max_sum), abs(cnt - min_sum))
    
    min_sum = min(cnt, min_sum)
    max_sum = max(cnt, max_sum)
print(res)

    