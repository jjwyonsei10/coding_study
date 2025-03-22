import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[1])
d1, d2 = 0,0
cnt = 0
for start, end in arr:
    if start < d1:
        continue
    if start < d2:
        d1 = d2
        d2 = end
        cnt+=1
    else:
        d2 = end
        cnt+=1
print(cnt)