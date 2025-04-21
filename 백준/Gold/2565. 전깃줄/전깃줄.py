n = int(input())
lista = []
for _ in range(n):lista.append(list(map(int, input().split())))
lista.sort()
dp = [1] * (n)
for i in range(1, n):
    for j in range(i):
        if lista[i][1] > lista[j][1]:dp[i] = max(dp[i], dp[j]+1)
print(n- max(dp))