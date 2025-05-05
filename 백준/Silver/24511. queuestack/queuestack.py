from collections import deque
moi = lambda: map(int, input().split())
n = int(input())
ds = list(moi())
ds_v = list(moi())
m = int(input())
val = list(moi())
q = deque()
check = 0
for i in range(n):
    if not ds[i]:
        q.appendleft(ds_v[i])
    else:
        check+=1
if check == n:
    print(*val)
else:
    for i in range(m):
        print(q.popleft(), end= ' ')
        q.append(val[i])