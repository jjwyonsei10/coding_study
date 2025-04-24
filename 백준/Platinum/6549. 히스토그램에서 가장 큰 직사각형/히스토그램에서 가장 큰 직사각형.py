moi = lambda: map(int, input().split())
while True:
    n, *arr = moi()
    if n == 0:
        break
    arr.append(0)
    stack = []
    res = 0
    for i in range(n + 1):
        while stack and arr[stack[-1]] > arr[i]:
            ind = stack.pop()
            # 왼쪽 경계를 스택의 새로운 최상단에서 가져옴
            width = i if not stack else i - stack[-1] - 1
            res = max(res, arr[ind] * width)
        stack.append(i)
    print(res)
