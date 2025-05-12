import math
n = int(input())
mod = 1000000007
total = 0

def multi(x, exp):
    if exp == 1:
        return x
    if exp %2 == 0:
        half = multi(x, exp//2)
        return half * half % mod
    else:
        return x * multi(x, exp-1)% mod


for _ in range(n):
    b,a = map(int, input().split())
    gcd = math.gcd(a,b) #기약 분수 조건
    a //= gcd
    b //= gcd
    total += a * multi(b, mod-2) % mod
    total %= mod
print(total)