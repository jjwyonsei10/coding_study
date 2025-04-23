n = int(input())
dist = list(map(int, input().split()))
val = list(map(int, input().split()))
stack = []
res = 0
for i in range(n-1):
    if stack and val[stack[-1]] > val[i]:
        v = stack.pop()
        res += val[v] * sum(dist[v:i])
        stack.append(i)
    elif len(stack) == 0:
        stack.append(i)
if stack:
    res+= val[stack[-1]] * sum(dist[stack[-1]:n-1])
print(res)