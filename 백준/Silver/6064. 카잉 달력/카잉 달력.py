import sys
import math
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,m,x,y = map(int, input().split())
    #1,1/ 2,2, 3,3/ 4,4, 5,5/ 6,6, 7,7/ 8,8
    # 9,9/ 10,10/1,11/ 2, 12/ 3, 1/ 
    max_year = math.lcm(n,m)
    ans = x
    while ans<= max_year:
        if (ans - 1) % m + 1 == y:
            break
        ans += n
    if ans > max_year:
        print(-1)
    else:
        print(ans)
