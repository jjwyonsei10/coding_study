import sys
input = sys.stdin.readline
moi = lambda: map(int, input().split())
n = int(input())

arr = list(moi())
arr.sort()
dp = [0] * (n)
dp[0] = arr[0]
for i in range(1, n):
    dp[i] = dp[i-1] + arr[i]

print(sum(dp))