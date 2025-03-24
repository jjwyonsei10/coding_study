import sys
sys.setrecursionlimit(10000000)

input = sys.stdin.readline

n = int(input())

moi = lambda: map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = moi()
    graph[a].append(b)
    graph[b].append(a)

dp = [[0, 1] for _ in range(n + 1)]
stack = []
parent = [-1] * (n + 1)  # 부모 노드를 저장

# 스택을 이용한 DFS
def dfs_stack(root):
    stack.append(root)
    order = []  # 처리 순서를 기록

    while stack:
        node = stack.pop()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor != parent[node]:  # 부모 노드가 아니면 자식으로 탐색
                parent[neighbor] = node
                stack.append(neighbor)

    # 역순으로 dp 값을 계산
    for node in reversed(order):
        for child in graph[node]:
            if child != parent[node]:  # 자식 노드만 고려
                dp[node][0] += dp[child][1]  # 현재 노드가 얼리 어답터가 아닐 경우
                dp[node][1] += min(dp[child])  # 현재 노드가 얼리 어답터일 경우

dfs_stack(1)
print(min(dp[1]))
