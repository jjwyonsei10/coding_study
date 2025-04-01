import sys
input = sys.stdin.readline

moi = lambda: map(int, input().split())

N, T = moi()

arr = [list(moi()) for _ in range(N)]
dis = list(moi())  # 피로도

# DP 및 추적 배열 초기화
dp = [-float('inf')] * (T+1)
dp[0] = 0
track = [[0] * (T+1) for _ in range(N)]

# DP 진행
for i in range(N):  # 과목별
    prev_dp = dp[:]  # 이전 DP 상태 저장
    for j in range(T, -1, -1):  # 총 공부 시간 역순 탐색
        for k in range(j, -1, -1):  # 해당 과목에서 가능한 공부 시간 역순 탐색
            new_cost = prev_dp[j - k] + arr[i][k]  # 이전 DP 값을 사용
            if dp[j] < new_cost:
                dp[j] = new_cost
                track[i][j] = k  # 최적 공부 시간 저장

# 피로도 적용 후 최대 점수 찾기
max_score = -float('inf')
best_time = 0

for i in range(T+1):
    final_score = dp[i] - dis[i]
    if final_score > max_score:
        max_score = final_score
        best_time = i

# 역추적하여 공부 계획 찾기
study_time = [0] * N
remaining_time = best_time

for i in range(N-1, -1, -1):  # 역추적 (과목별 최적 공부 시간 찾기)
    study_time[i] = track[i][remaining_time]
    remaining_time -= study_time[i]

# 출력
print(max_score)
print(*study_time)
