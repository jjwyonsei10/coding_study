import heapq
n = int(input())
lista = []

for _ in range(n):
    arr = list(map(int, input().split()))
    if not lista:
        for a in arr:
            heapq.heappush(lista, a)
    else:
        for a in arr:
            if lista[0] < a:
                heapq.heappush(lista, a)
                heapq.heappop(lista)
print(lista[0])