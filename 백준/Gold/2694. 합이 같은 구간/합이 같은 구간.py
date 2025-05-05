import sys
input = sys.stdin.readline
train = int(input())
for t in range(train):
    n = int(input())
    arr = list()
    cnt  = n//10 + 1 if n%10 else n//10
    for _ in range(cnt): arr += list(map(int, input().split()))
    dp = [0] * (n)
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = dp[i-1] + arr[i]
    total_sum = dp[-1]

    # 조건에 맞는 값 찾기
    for ind in dp:
        if total_sum % ind == 0:  # ind가 총합을 나눌 수 있는지 확인
            cnt = 0
            for value in dp:
                if value % ind == 0:  # ind로 나눠지는 누적 합의 개수 세기
                    cnt += 1
            if cnt == total_sum // ind:  # 조건 만족 시 ind 출력
                print(ind)
                break