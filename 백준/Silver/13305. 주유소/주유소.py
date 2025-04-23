n = int(input())
dist = list(map(int, input().split()))
val = list(map(int, input().split()))

init = dist[0] * val[0]

for i in range(1, n):
    if val[i] == min(val[:n-1]):
        init+= val[i] * sum(dist[i:n-1])
        break
    else:
        init+= val[i] * dist[i]
print(init)