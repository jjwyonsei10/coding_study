import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

moi = lambda: map(int, input().split())
n,m = moi()
x,y = 0,0
xdict, ydict = {}, {}
for _ in range(n):
    a,b  = moi()
    if xdict.get(a):
        xdict[a].append(b)
    else:
        xdict[a] = [b]
    if ydict.get(b):
        ydict[b].append(a)
    else:
        ydict[b] = [a]
string = input().rstrip()

for k,v in xdict.items():
    xdict[k] = sorted(v)
for k,v in ydict.items():
    ydict[k] = sorted(v)

for s in string:
    if s == "R":
        x =ydict[y][bisect_right(ydict[y], x)]
    elif s == "L":
        x =ydict[y][bisect_left(ydict[y], x)-1]
    elif s == "U":
        y =xdict[x][bisect_right(xdict[x], y)] #x축의값을 기준으로 y축의 값보다 큰 처음 좌표를 가진다
    else:
        y =xdict[x][bisect_left(xdict[x], y)-1] #x축의 값을 기준으로 y축 값보다 작은 최대 좌표를 찾는다
print(x,y)