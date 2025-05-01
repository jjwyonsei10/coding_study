n = int(input())
weight1 = list(map(int, input().split()))
m = int(input())
weight2 = list(map(int, input().split()))
dp = [[0] * (15001) for _ in range(31)]
def dfs(num, weight):
    if num > n: return 
    if dp[num][weight]: return
    dp[num][weight] = 1
    dfs(num+1, weight + weight1[num-1])
    dfs(num+1, abs(weight - weight1[num-1]))
    dfs(num+1, weight) #이걸로 그냥 똑같은 경우 다 되는거긴 하네
dfs(0,0)
for weight in weight2:
    if weight > 15000: print("N", end = " ")
    elif dp[n][weight]: print("Y",end = " ")
    else: print("N",end = " ")