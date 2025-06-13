import sys
input =sys.stdin.readline
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 초기 상어 위치 및 초기 크기 설정
x, y, size = 0, 0, 2
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            x, y = i, j
            arr[x][y] = 0  # 상어 초기 위치를 빈칸으로 초기화

shark_eat = 0
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]  # 상하좌우 방향 벡터

def bfs(x, y):
    q = deque([(x, y)])
    visit = [[False] * n for _ in range(n)]
    dist = [[0] * n for _ in range(n)]
    visit[x][y] = True
    edible_fish = []

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                if arr[nx][ny] <= size:  # 이동 가능한 조건
                    visit[nx][ny] = True
                    dist[nx][ny] = dist[cx][cy] + 1
                    q.append((nx, ny))
                    # 먹을 수 있는 물고기
                    if 0 < arr[nx][ny] < size:
                        edible_fish.append((nx, ny, dist[nx][ny]))

    # 거리가 가까운 순, 행이 작은 순, 열이 작은 순으로 정렬
    return sorted(edible_fish, key=lambda fish: (fish[2], fish[0], fish[1]))

total_time = 0

while True:
    fishes = bfs(x, y)
    if not fishes:  # 먹을 수 있는 물고기가 없으면 종료
        print(total_time)
        break

    # 가장 가까운 물고기 선택
    x, y, distance = fishes[0]
    arr[x][y] = 0  # 물고기 먹은 자리 초기화
    total_time += distance

    shark_eat += 1
    if shark_eat == size:  # 상어가 현재 크기만큼 먹으면 크기 증가
        shark_eat = 0
        size += 1
