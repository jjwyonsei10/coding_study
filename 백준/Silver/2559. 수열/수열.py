import sys
input = sys.stdin.readline
moi = lambda: map(int, input().split())
n,k = moi()
lista = list(moi())
ans = []
ans.append(sum(lista[:k]))
for i in range(n-k):ans.append(ans[i] - lista[i] + lista[i+k])
print(max(ans))