def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    a = find(a)
    b = find(b)
    if a in known and b in known:
        return
    if a in known:
        parent[b] = a
    elif b in known:
        parent[a] = b
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
moi = lambda: map(int, input().split())
n,m = moi()
parent = [i for i in range(n+1)]
known = list(moi())[1:]
parties = []
for _ in range(m):
    q = list(moi())
    l = q[0]
    q_lists = q[1:]
    for i in range(l-1):
        union(q_lists[i], q_lists[i+1])
    parties.append(q_lists)
ans = 0
for p in parties:
    for i in range(len(p)):
        if find(p[i]) in known:break
    else:ans+=1
print(ans)