import sys
import heapq
input = sys.stdin.readline
t = int(input())
lista = []
for _ in range(t):
    n = int(input())
    if n == 0:
        if not len(lista):
            print(0)
        else:
            q = -heapq.heappop(lista)
            print(q)
    else:
        heapq.heappush(lista, -n)
