n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
z = 0
o = 0

def sol(x,y,n):
    global z,o
    col = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j]!= col:
                sol(x,y, n//2)
                sol(x,y+n//2, n//2)
                sol(x+n//2,y, n//2)
                sol(x+n//2,y+n//2, n//2)
                return
    if col == 0:
        z+=1
    else:
        o+=1
sol(0,0,n)
print(z)
print(o)