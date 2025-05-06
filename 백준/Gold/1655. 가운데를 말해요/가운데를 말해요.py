import sys
import heapq
input = sys.stdin.readline
n = int(input())
l,r = [],[] #하나는 maxheap, 하나는 minheap을 고려한다
for _ in range(n):
    m = int(input())
    if len(l) > len(r):
        heapq.heappush(r, m)
    elif len(l) == len(r):
        heapq.heappush(l, -m)

    if r and -l[0] > r[0]:
        left = heapq.heappop(l)
        right = heapq.heappop(r)
        heapq.heappush(r, -left)
        heapq.heappush(l, -right)
    print(-l[0])