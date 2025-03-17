n,m,q = map(int, input().split())
row = [0] * n
col = [0] * m

for _ in range(q):
    c,r,v = map(int, input().split())
    if c == 1:
        row[r-1]+=v
    else:
        col[r-1]+=v


for i in range(n):
    for j in range(m):
        print(row[i] + col[j], end = " ")
    print("")
