import heapq
n,m = map(int, input().split())
jew = []
for _ in range(n):heapq.heappush(jew, list(map(int, input().split())))
bags = []
for _ in range(m):heapq.heappush(bags, int(input()))
bags.sort()
ans = 0
tmp_jews = []
for bag in bags:
    while jew and bag >= jew[0][0]:heapq.heappush(tmp_jews, -heapq.heappop(jew)[1])
    if tmp_jews:ans+= -heapq.heappop(tmp_jews)
    elif not jew:break
print(ans)