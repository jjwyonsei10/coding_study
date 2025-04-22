from collections import defaultdict
import sys
input = sys.stdin.readline

# 입력 처리
moi = lambda: map(int, input().split())
n, m = moi()
arr = list(moi())

# 누적합의 나머지를 저장할 리스트
dp = [0]
for i in range(n):
    dp.append((dp[-1] + arr[i]) % m)

# 나머지 등장 횟수 카운트
my_dict = defaultdict(int)
for d in dp:
    my_dict[d] += 1

# 조합 계산: 같은 나머지가 v개 있으면 vC2 = v * (v - 1) // 2
res = 0
for v in my_dict.values():
    res += v * (v - 1) // 2

print(res)
