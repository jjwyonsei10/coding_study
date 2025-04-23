import sys
input = sys.stdin.readline
n,m,c = map(int, input().split())
def cal(a,b,c):
    if b == 1:
        return a%c
    tmp = cal(a, b//2, c)
    if b %2 == 0:
        return tmp * tmp % c
    else:
        return tmp * tmp % c * a % c
print(cal(n,m,c))