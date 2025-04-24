n = int(input())
mod = 1000000007
memo = {}

memo[0] = 0
memo[1] = memo[2] = 1

def dp(i):
    if i not in memo:
        if i %2 == 0:memo[i] = dp(i//2) * (dp(i//2) + 2 * dp(i//2 -1)) % mod
        else:memo[i] = (dp(i//2) **2 + dp(i//2 +1) ** 2) % mod
    return memo[i]

print(dp(n))