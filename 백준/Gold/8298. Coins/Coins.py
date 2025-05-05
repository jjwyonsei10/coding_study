n, m = map(int, input().split())
str = input().rstrip()
dp = 0
dic = {0:0}
res = 0
for i in range(1, n+1):
    if str[i-1] == "R":
        dp+=m
    else:
        dp-=1
    if dp not in dic:
        dic[dp] = i
    else:
        res = max(res, i - dic[dp])
print(res)