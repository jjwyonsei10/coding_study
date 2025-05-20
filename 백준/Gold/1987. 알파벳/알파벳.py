import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, visit, cnt):
    global max_len
    q = deque()
    q.append((x, y, visit, cnt))

    visited = set()
    visited.add((x, y, visit))

    while q:
        x, y, visit, cnt = q.popleft()
        max_len = max(max_len, cnt)

        for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= nx < n and 0 <= ny < m:
                alpha = ord(arr[nx][ny]) - ord('A')
                if not (visit & (1 << alpha)):
                    new_visit = visit | (1 << alpha)
                    if (nx, ny, new_visit) not in visited:
                        visited.add((nx, ny, new_visit))
                        q.append((nx, ny, new_visit, cnt + 1))

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

start = ord(arr[0][0]) - ord("A")
max_len = 1
bfs(0, 0, 1 << start, 1)
print(max_len)
