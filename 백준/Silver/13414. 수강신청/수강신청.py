import sys
from collections import deque

input = sys.stdin.readline

moi = lambda : map(int, input().split())

n,m = moi()

q = dict()

for i in range(m):
    x = input().rstrip()
    q[x] = i

q1 = sorted(q.items(), key = lambda x:x[1])
if len(q1) < n:
    n = len(q1)
for i in range(n):
    print(q1[i][0])