n = int(input())
arr = list(map(int, input().split()))
stack = []
rec = [-1] * (n)
for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        rec[stack[-1]] = arr[i]
        stack.pop()
    stack.append(i)
print(*rec)