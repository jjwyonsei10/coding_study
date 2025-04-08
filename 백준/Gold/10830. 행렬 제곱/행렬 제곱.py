import sys
input = sys.stdin.readline
moi = lambda: map(int, input().split())
n,a = moi()
arr = [list(moi()) for _ in range(n)]


def multi_arr(a,b):
    x = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                x[i][j] += (a[i][k] * b[k][j] % 1000)
    return x

def square(x, n):
    if n == 1:
        return x
    temp = square(x, n//2)
    if n % 2:
        return multi_arr(multi_arr(temp, temp) , x)
    else:
        return multi_arr(temp, temp)
    
result = square(arr, a)

for i in range(n):
    for j in range(n):
        result[i][j] %=1000

for r in result:
    print(*r)
