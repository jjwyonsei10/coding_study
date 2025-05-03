n = int(input())
heights = [int(input()) for _ in range(n)]
heights.append(0)  # 마지막에 0 추가하여 스택을 비울 수 있게 처리
stack = []
res = 0

for i in range(n + 1):
    while stack and heights[stack[-1]] > heights[i]:
        h = heights[stack.pop()]  # 현재 높이
        w = i if not stack else i - stack[-1] - 1  # 너비 계산
        res = max(res, h * w)
    stack.append(i)

print(res)
