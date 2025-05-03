n = int(input())
arr = list(map(int, input().split()))
arr_dict = {}
for a in arr:
    if a not in arr_dict:
        arr_dict[a]=1
    else:
        arr_dict[a]+=1
rec  = [-1] * n
stack = []

for i in range(n):
    while stack and arr_dict[arr[stack[-1]]] < arr_dict[arr[i]]:
        rec[stack[-1]] = arr[i]
        stack.pop()
    stack.append(i)
print(*rec)