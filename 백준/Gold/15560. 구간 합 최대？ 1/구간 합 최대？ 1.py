import sys
input = sys.stdin.readline

moi = lambda: map(int, input().split())

N,Q,U,V = moi()
k = list(moi())
for _ in range(Q):
    ans = float('-inf')
    c,a,b = moi()
    if c == 0:
        for i in range(a-1,b):
            total = 0
            for j in range(i, b):
                total+= k[j]
                val = total*U + (j-i)* V
                ans = max(ans, val) 
        print(ans)
    else:k[a-1]  = b
