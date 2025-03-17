n,m = map(int, input().split())
res = 1e9

arr = [list(input().rstrip()) for _ in range(n)]

def check(x,y):
    global res
    check = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if (i+j) % 2:
                if arr[i][j] == 'W':
                    check+=1
            else:
                if arr[i][j] == 'B':
                    check+=1
    ans = min(check, 64- check)
    res = min(ans, res)

for i in range(n-7):
    for j in range(m-7):
        check(i,j)
print(res)