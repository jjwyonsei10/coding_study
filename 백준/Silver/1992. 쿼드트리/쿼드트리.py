n = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
res = []
def sol(x,y,n):
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != color:
                res.append("(")
                sol(x, y, n//2)
                sol(x, y+n//2, n//2)    
                sol(x+n//2, y, n//2)
                sol(x+n//2, y+n//2, n//2)
                res.append(")")
                return
    res.append(color)
sol(0,0,n)
print(*res, sep="")
    