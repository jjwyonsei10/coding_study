n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
m,z,o = 0,0,0

def sol(x,y,n):
    global m,z,o
    col = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if col != arr[i][j]:
                sol(x,y,n//3)
                sol(x+n//3,y,n//3)
                sol(x+2*n//3,y,n//3)
                sol(x,y+n//3,n//3)
                sol(x,y+2*n//3,n//3)
                sol(x+n//3,y+n//3,n//3)
                sol(x+n//3,y+2*n//3,n//3)
                sol(x+2*n//3,y+n//3,n//3)
                sol(x+2*n//3,y+2*n//3,n//3)
                return
    if col == -1:m+=1
    elif col == 0:z+=1
    else:o+=1

sol(0,0,n)
print(m)
print(z)
print(o)