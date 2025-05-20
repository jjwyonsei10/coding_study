#하지만 위의 2가지 방법들은 각각 26!가 발생하는 경우로 인하여 일반적인 풀이가 될 수 없다.
#gpt의 풀이: 비트 마스킹

import sys
input = sys.stdin.readline
from collections import deque

def bfs(x,y,visit, cnt):
    global max_len

    q = deque()
    q.append((x,y, visit, cnt))

    visited = set()
    visited.add((x,y,visit))

    while q:
        x,y,visit, cnt = q.popleft()
        max_len =max(max_len, cnt)

        for nx, ny in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
            if 0<=nx<n and 0<=ny<m:
                alpha = ord(arr[nx][ny]) - ord('A')
                if not (visit & (1<< alpha)):
                    new_visit = visit|(1<<alpha)
                    if (nx, ny, new_visit) not in visited:
                        visited.add((nx, ny, new_visit))
                        q.append((nx, ny, new_visit, cnt+1))

n,m = map(int, input().split())
arr  = [list(input().rstrip()) for _ in range(n)]
max_ = 1
start = ord(arr[0][0]) - ord("A")
max_len = 1
bfs(0,0,1<<start, max_len)
print(max_len)