t = int(input())
for _ in range(t):
    x1,y1, x2,y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for i in range(n):
        cx,cy,cr =  map(int, input().split())
        dist1 = (x1-cx) **2 + (y1-cy)**2 
        dist2 = (x2-cx) **2 + (y2-cy)**2
        if (dist1 < cr**2 and dist2 > cr**2) or  (dist1 > cr**2 and dist2 < cr**2):
           cnt+=1
    print(cnt) 