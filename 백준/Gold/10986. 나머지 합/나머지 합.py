from collections import defaultdict
import sys
input = sys.stdin.readline

# 입력 처리
moi = lambda: map(int, input().split())
n, m = moi()
arr = list(moi())
my_dict = defaultdict(int)
res = 0
cur_sum = 0
my_dict[0] = 1
for num in arr:
    cur_sum+=num
    mod = cur_sum%m
    res+= my_dict[mod]
    my_dict[mod]+=1
print(res)